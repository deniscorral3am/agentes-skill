# Agentes · skill de Claude Code

7 agentes de Claude que puedes crear en 10 minutos. Le cuentas a Claude qué vendes y a quién, y te deja montados los 7,
adaptados a tu negocio:

| # | Agente | Comando | Qué hace |
|---|---|---|---|
| 01 | Contenido | `/agente-contenido` | investiga tu nicho → guion con gancho y CTA → plan de edición → copy listo |
| 02 | Setter 24/7 | `/agente-setter` | contesta DMs → cualifica → agenda solo a los que encajan |
| 03 | Busca clientes | `/agente-prospeccion` | busca empresas reales → investiga cada una → primer mensaje personalizado |
| 04 | Resume reuniones | `/agente-reuniones` | lee la transcripción → resumen con dolores y objeciones → email de seguimiento |
| 05 | Atención al cliente | `/agente-atencion` | entiende → consulta tu base de conocimiento → responde (o pasa a humano) |
| 06 | Tu asistente personal | `/agente-asistente` | correo · calendario · avisos de lo que se te pasa |
| 07 | Finanzas | `/agente-finanzas` | facturas → caja por mes → alertas de impagos y gastos |

Hecha por [Denis Corral · Sell Your AI](https://sellyourai.io).

## Qué necesitas

- [Claude Code](https://claude.com/claude-code)
- Python 3 (solo librería estándar)
- Opcional: conectores de Gmail y Google Calendar en Claude para el asistente personal.

## Instalación

```bash
git clone https://github.com/deniscorral3am/agentes-skill.git ~/.claude/skills/agentes
```

## Uso

1. En Claude Code escribe `/agentes`.
2. Contesta 4 preguntas (qué vendes y a quién, por dónde te llegan los clientes, tu tono y qué agentes quieres).
3. Claude guarda el perfil de tu negocio en `~/.claude/agentes/perfil.md`, instala los agentes y prueba cada uno.

Después, llama a cada agente por su comando (o pídeselo con tus palabras: «contesta este DM», «cómo voy de caja»).
Lo que hacen se guarda en `~/Desktop/Agentes/<agente>/`. Si cambia tu oferta, cambia el perfil y los 7 se enteran.

Ningún agente envía, publica ni paga nada por su cuenta: te deja el borrador y te pide el OK.

## Estructura

- `SKILL.md`: el instalador (preguntas, perfil, instalación, pruebas)
- `plantillas/<agente>/SKILL.md`: los 7 agentes
- `ref/perfil.md`: plantilla del perfil del negocio
- `motor/instalar.py`: copia los agentes a `~/.claude/skills/`
- `motor/caja.py`: caja y alertas desde un CSV de movimientos (`python3 motor/caja.py --ejemplo`)

¿Quieres que estos agentes trabajen para tus clientes y cobrar por ello? Eso es [Sell Your AI](https://sellyourai.io).
