#!/usr/bin/env python3
"""Caja y alertas a partir de un CSV de movimientos o facturas (solo librería estándar).

Columnas (cabecera; se aceptan sinónimos): fecha, concepto, importe, tipo (ingreso/gasto), estado (pagada/pendiente),
vencimiento, cliente. Importe en euros con coma o punto; si no hay «tipo», el signo manda (negativo = gasto).

  python3 caja.py movimientos.csv [--saldo 12000] [--json salida.json]
  python3 caja.py --ejemplo            -> genera y analiza un CSV de ejemplo
"""
import argparse, csv, json, re, sys, tempfile
from collections import defaultdict
from datetime import date, datetime, timedelta

SIN = {'fecha': ['fecha', 'date', 'dia'], 'concepto': ['concepto', 'descripcion', 'descripción', 'detalle', 'concept'],
       'importe': ['importe', 'cantidad', 'total', 'amount', 'euros'], 'tipo': ['tipo', 'type'],
       'estado': ['estado', 'status'], 'vencimiento': ['vencimiento', 'vence', 'due', 'due_date'],
       'cliente': ['cliente', 'proveedor', 'contacto', 'client']}


def num(s):
    s = re.sub(r'[^\d,.\-]', '', str(s or ''))
    if not s: return 0.0
    if ',' in s and '.' in s: s = s.replace('.', '').replace(',', '.') if s.rfind(',') > s.rfind('.') else s.replace(',', '')
    elif ',' in s: s = s.replace(',', '.')
    return float(s)


def fecha(s):
    for f in ('%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y'):
        try: return datetime.strptime(str(s).strip(), f).date()
        except ValueError: pass
    return None


def leer(ruta):
    with open(ruta, newline='', encoding='utf-8-sig') as f:
        muestra = f.read(4096); f.seek(0)
        filas = list(csv.DictReader(f, dialect=csv.Sniffer().sniff(muestra, ';,\t')))
    cab = {k.lower().strip(): k for k in filas[0]} if filas else {}
    col = {c: next((cab[s] for s in ss if s in cab), None) for c, ss in SIN.items()}
    if not col['importe']: sys.exit(f'No encuentro la columna de importe. Cabecera: {list(cab)}')
    out = []
    for r in filas:
        imp = num(r[col['importe']])
        tipo = (r.get(col['tipo']) or '').lower() if col['tipo'] else ''
        gasto = 'gasto' in tipo or 'pago' in tipo or (not tipo and imp < 0)
        out.append({'fecha': fecha(r.get(col['fecha'])) if col['fecha'] else None,
                    'concepto': (r.get(col['concepto']) or '').strip() if col['concepto'] else '',
                    'cliente': (r.get(col['cliente']) or '').strip() if col['cliente'] else '',
                    'importe': -abs(imp) if gasto else abs(imp),
                    'pendiente': 'pend' in ((r.get(col['estado']) or '').lower() if col['estado'] else ''),
                    'vence': fecha(r.get(col['vencimiento'])) if col['vencimiento'] else None})
    return out


def analizar(movs, saldo=None, hoy=None):
    hoy = hoy or date.today()
    cobrado = [m for m in movs if m['importe'] > 0 and not m['pendiente']]
    gastos = [m for m in movs if m['importe'] < 0 and not m['pendiente']]
    por_mes = defaultdict(lambda: [0.0, 0.0])
    for m in cobrado + gastos:
        if m['fecha']: por_mes[m['fecha'].strftime('%Y-%m')][0 if m['importe'] > 0 else 1] += m['importe']
    meses = sorted(por_mes)
    gasto_medio = -sum(por_mes[k][1] for k in meses[-3:]) / max(1, len(meses[-3:]))
    alertas = []
    for m in movs:
        if m['pendiente'] and m['importe'] > 0 and m['vence'] and (hoy - m['vence']).days > 0:
            d = (hoy - m['vence']).days
            alertas.append((3 if d > 30 else 2, f"Impago: {m['cliente'] or m['concepto']} · {m['importe']:.0f} € · vencida hace {d} días"))
    if len(meses) >= 2:
        a, b = -por_mes[meses[-2]][1], -por_mes[meses[-1]][1]
        if a and b > a * 1.25: alertas.append((2, f'Los gastos de {meses[-1]} suben un {100 * (b / a - 1):.0f} % ({a:.0f} → {b:.0f} €)'))
    rep = defaultdict(list)
    for m in gastos: rep[(m['concepto'].lower()[:25], round(m['importe']))].append(m)
    for (c, imp), ms in rep.items():
        veces = defaultdict(int)
        for x in ms:
            if x['fecha']: veces[x['fecha'].strftime('%Y-%m')] += 1
        for mes, n in sorted(veces.items()):
            if c and n > 1:
                alertas.append((1, f'Posible cargo duplicado: «{ms[0]["concepto"]}» {-imp} € ({n} veces en {mes})'))
    pend = sum(m['importe'] for m in movs if m['pendiente'] and m['importe'] > 0)
    res = {'meses': {k: {'ingresos': round(v[0], 2), 'gastos': round(-v[1], 2), 'neto': round(v[0] + v[1], 2)} for k, v in sorted(por_mes.items())},
           'por_cobrar': round(pend, 2), 'gasto_medio_mensual': round(gasto_medio, 2),
           'alertas': [t for _, t in sorted(alertas, key=lambda x: -x[0])]}
    if saldo is not None and gasto_medio:
        res['saldo'] = saldo; res['meses_de_caja'] = round(saldo / gasto_medio, 1)
    return res


def imprimir(r):
    print('MES       INGRESOS    GASTOS      NETO')
    for k, v in r['meses'].items(): print(f"{k}  {v['ingresos']:>9.0f} € {v['gastos']:>8.0f} € {v['neto']:>8.0f} €")
    print(f"\nPor cobrar: {r['por_cobrar']:.0f} €   ·   Gasto medio (3 últimos meses): {r['gasto_medio_mensual']:.0f} €/mes")
    if 'meses_de_caja' in r: print(f"Con {r['saldo']:.0f} € en banco tienes {r['meses_de_caja']} meses de caja")
    print('\nALERTAS' if r['alertas'] else '\nSin alertas.')
    for a in r['alertas']: print('  ! ' + a)


def ejemplo():
    h = date.today().replace(day=1)
    m = lambda n: (h - timedelta(days=30 * n)).replace(day=5)
    filas = [('fecha', 'concepto', 'cliente', 'importe', 'tipo', 'estado', 'vencimiento')]
    for n in (2, 1, 0):
        filas += [(m(n), 'Cuota mensual', 'Clínica Norte', '1500', 'ingreso', 'pagada', m(n)),
                  (m(n), 'Herramientas IA', '', '-180', 'gasto', 'pagada', ''),
                  (m(n), 'Anuncios Meta', '', str(-400 - 250 * (n == 0)), 'gasto', 'pagada', '')]
    filas += [(m(0), 'Herramientas IA', '', '-180', 'gasto', 'pagada', ''),
              (m(1), 'Proyecto web', 'Taller López', '900', 'ingreso', 'pendiente', m(1) + timedelta(days=15))]
    f = tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False, newline='')
    csv.writer(f).writerows(filas); f.close()
    print(f'(CSV de ejemplo en {f.name})\n')
    return f.name


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('csv', nargs='?'); ap.add_argument('--saldo', type=float); ap.add_argument('--json')
    ap.add_argument('--ejemplo', action='store_true')
    a = ap.parse_args()
    ruta = ejemplo() if a.ejemplo else a.csv
    if not ruta: ap.error('pasa un CSV o --ejemplo')
    r = analizar(leer(ruta), 6000 if a.ejemplo and a.saldo is None else a.saldo)
    imprimir(r)
    if a.json: json.dump(r, open(a.json, 'w'), ensure_ascii=False, indent=2)
