---
name: agentes
description: Instala en 10 minutos los 7 agentes de Claude para un negocio (contenido, setter 24/7, busca clientes, resume reuniones, atención al cliente, asistente personal y finanzas), ya adaptados a su oferta, su cliente y su tono. Hace 4 preguntas, guarda el perfil del negocio y deja cada agente como una skill propia (/agente-contenido, /agente-setter…), probada. Úsala cuando digan /agentes, «comenta AGENTES», «los 7 agentes de Claude», «móntame los agentes» o «quiero agentes para mi negocio».
---

# /agentes: los 7 agentes de Claude en 10 minutos

Idea: no hacen falta 7 herramientas ni n8n para empezar. Cada agente es una skill de Claude Code que conoce tu negocio
(lo lee de un perfil común) y hace un trabajo de principio a fin. Instalas una vez y los llamas cuando los necesitas.

Perfil del negocio: `~/.claude/agentes/perfil.md` (plantilla en `ref/perfil.md`) · Plantillas de los agentes:
`plantillas/<agente>/SKILL.md` · Instalador: `motor/instalar.py` · Salidas de los agentes: `~/Desktop/Agentes/<agente>/`.

| # | Agente | Skill | Qué hace |
|---|---|---|---|
| 01 | Contenido | `/agente-contenido` | investiga → guion → edita → publica |
| 02 | Setter 24/7 | `/agente-setter` | DMs → cualifica → agenda |
| 03 | Busca clientes | `/agente-prospeccion` | busca → investiga → escribe |
| 04 | Resume reuniones | `/agente-reuniones` | escucha → resume → seguimiento |
| 05 | Atención al cliente | `/agente-atencion` | entiende → consulta → responde |
| 06 | Tu asistente personal | `/agente-asistente` | mail · calendario · avisos |
| 07 | Finanzas | `/agente-finanzas` | facturas → caja → alertas |

## 01 · Las 4 preguntas (minuto 0–4)
Si ya existe `~/.claude/agentes/perfil.md`, leerlo, enseñar un resumen de 3 líneas y preguntar solo si quiere cambiar
algo. Si no, AskUserQuestion en una tanda (opciones sacadas de lo que ya haya contado; siempre cabe «Otro»):
1. **Qué vendes y a quién**: oferta, precio aproximado, cliente ideal y para quién NO es.
2. **Por dónde te llegan los clientes**: Instagram (comentarios/DMs), WhatsApp, anuncios con formulario, web, puerta fría
   (LinkedIn, email). Varias.
3. **Tono**: tú/usted, cercano o serio, emojis sí/no, una frase que digas siempre.
4. **Qué agentes quieres hoy**: los 7 (recomendado) o los que elija.
Después, en texto libre y opcional: enlace de calendario, web, 2–3 casos o resultados reales, herramientas que ya usa
(Gmail, Google Calendar, Fathom, Notion, Holded…). Si dice «tú decides», elegir lo prudente y apuntarlo.

## 02 · Guardar el perfil (minuto 4–6)
Escribir `~/.claude/agentes/perfil.md` siguiendo `ref/perfil.md`, con sus palabras literales. Lo que no dio queda como
`PENDIENTE` (nunca inventar casos, cifras ni enlaces). Crear `~/.claude/agentes/conocimiento/` (para el agente de
atención) y meter ahí lo que haya pasado: FAQ, precios, condiciones, web copiada.

## 03 · Instalar (minuto 6–7)
`python3 ~/.claude/skills/agentes/motor/instalar.py [--solo contenido,setter,...]`
Copia cada plantilla a `~/.claude/skills/<agente>/` y crea `~/Desktop/Agentes/<agente>/`. Si un agente ya existe no lo
pisa (lo dice); para reinstalar, `--forzar`.

## 04 · Probar cada agente (minuto 7–10)
Una prueba corta y real por agente instalado, con su perfil, y enseñar el resultado en 2–4 líneas:
- contenido: 3 ganchos para su cliente ideal · setter: responder a un DM típico de su canal · prospección: 3 empresas
  reales que encajan (con fuente) · reuniones: si tiene una transcripción, resumirla; si no, explicar cómo pasarla ·
  atención: responder una pregunta frecuente usando `conocimiento/` · asistente: si tiene Gmail/Calendar conectados,
  la agenda de hoy; si no, cómo conectarlos · finanzas: `python3 ~/.claude/skills/agentes/motor/caja.py --ejemplo`.
Si una prueba sale floja (genérica, sin su tono, inventa), corregir la plantilla instalada y repetir.

## 05 · Entregar
Corto: la tabla de agentes instalados con su comando, qué quedó `PENDIENTE` en el perfil y el siguiente paso más útil
(normalmente: «pásame tus DMs de esta semana y que el setter los conteste»).

## Reglas
- **Nunca inventar** cifras, casos, testimonios, empresas ni enlaces. Lo que no se sabe, `PENDIENTE` o se busca con fuente.
- Ningún agente **envía, publica, paga ni borra** nada por su cuenta: prepara el borrador y pide el OK.
- Todo en el idioma y las palabras del negocio, sin jerga técnica.
- El perfil es la única fuente de verdad: si cambia la oferta, se cambia el perfil y los 7 agentes se enteran solos.

Hecha por Denis Corral · [Sell Your AI](https://sellyourai.io).
