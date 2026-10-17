#!/usr/bin/env python3
"""Instala los agentes como skills de Claude Code.

  python3 instalar.py                         -> los 7
  python3 instalar.py --solo contenido,setter -> solo esos
  python3 instalar.py --forzar                -> reinstala aunque ya existan
"""
import argparse, shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = Path.home() / '.claude' / 'skills'
SALIDAS = Path.home() / 'Desktop' / 'Agentes'
PERFIL = Path.home() / '.claude' / 'agentes'

ap = argparse.ArgumentParser()
ap.add_argument('--solo', default='')
ap.add_argument('--forzar', action='store_true')
a = ap.parse_args()

todos = sorted(p.name for p in (RAIZ / 'plantillas').iterdir() if p.is_dir())
elegidos = [f'agente-{x.strip()}' for x in a.solo.split(',') if x.strip()] or todos
malos = [x for x in elegidos if x not in todos]
if malos:
    raise SystemExit(f'No existen: {", ".join(malos)}. Hay: {", ".join(t[7:] for t in todos)}')

(PERFIL / 'conocimiento').mkdir(parents=True, exist_ok=True)
if not (PERFIL / 'perfil.md').exists():
    shutil.copy(RAIZ / 'ref' / 'perfil.md', PERFIL / 'perfil.md')
    print(f'Perfil vacío creado en {PERFIL / "perfil.md"} (rellénalo o vuelve a /agentes)')

for nombre in elegidos:
    destino = SKILLS / nombre
    (SALIDAS / nombre[7:]).mkdir(parents=True, exist_ok=True)
    if destino.exists() and not a.forzar:
        print(f'  = /{nombre} ya estaba (usa --forzar para reinstalar)')
        continue
    if destino.exists():
        shutil.rmtree(destino)
    shutil.copytree(RAIZ / 'plantillas' / nombre, destino)
    print(f'  + /{nombre}')
print(f'Listo. Salidas en {SALIDAS}')
