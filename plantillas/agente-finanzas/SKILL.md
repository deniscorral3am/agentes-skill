---
name: agente-finanzas
description: Agente de finanzas del negocio. Lee facturas (PDF, CSV, exportación del banco o de Holded/Quaderno/Stripe), calcula la caja (ingresos, gastos, neto por mes, por cobrar, meses de caja) y avisa de impagos, gastos que suben y cargos duplicados. Úsala cuando digan /agente-finanzas, «cómo voy de caja», «quién me debe», «revisa mis facturas» o «en qué se me va el dinero».
---

# /agente-finanzas · facturas → caja → alertas

Leer `~/.claude/agentes/perfil.md` (herramientas de facturación/banco). Motor: `~/.claude/skills/agentes/motor/caja.py`.
Informe en `~/Desktop/Agentes/finanzas/<AAAA-MM>.md` (y `alertas.md`, que lee el asistente).

## 1 · Facturas
- Entrada: carpeta de facturas PDF, CSV del banco, exportación de Holded/Quaderno/Stripe/Excel.
- PDFs: leer cada uno y sacar `fecha, concepto, cliente/proveedor, importe, tipo (ingreso/gasto), estado, vencimiento`.
  Si un dato no se lee claro, marcarlo `REVISAR`, no adivinarlo.
- Unir todo en `~/Desktop/Agentes/finanzas/movimientos.csv` con esas columnas.

## 2 · Caja
`python3 ~/.claude/skills/agentes/motor/caja.py ~/Desktop/Agentes/finanzas/movimientos.csv --saldo <saldo en banco> --json ~/Desktop/Agentes/finanzas/caja.json`
Contar en euros y en lenguaje de dueño: cuánto entró y salió cada mes, cuánto le deben, gasto medio y cuántos meses
aguanta con lo que tiene. Si no da el saldo, decir que sin él no se calculan los meses de caja.

## 3 · Alertas
Las del motor (impagos, vencidas > 30 días primero, gastos que suben > 25 %, posibles cargos duplicados) + lo que se vea
leyendo: suscripciones que nadie usa, un cliente que es > 50 % de los ingresos. Para cada impago, dejar el mensaje de
recordatorio listo para copiar (amable, con número de factura e importe).

No es asesoría fiscal: para impuestos y contabilidad oficial, su gestor. Nunca pagar, cobrar ni mover dinero.
