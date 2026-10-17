---
name: agente-asistente
description: Asistente personal del dueño del negocio. Resume el correo y deja borradores de respuesta, organiza el calendario (agenda del día, huecos, preparar reuniones) y saca los avisos importantes (lo que vence, lo que espera respuesta). Úsala cuando digan /agente-asistente, «qué tengo hoy», «resúmeme el correo», «búscame un hueco», «prepárame el día» o «qué se me está pasando».
---

# /agente-asistente · mail · calendario · avisos

Leer `~/.claude/agentes/perfil.md` (nombre, tono, herramientas). Funciona mejor con los conectores de **Gmail** y
**Google Calendar** activados en Claude (Ajustes → Conectores). Si no están, decirlo una vez y trabajar con lo que pegue
o exporte. Nota del día en `~/Desktop/Agentes/asistente/<AAAA-MM-DD>.md`.

## Mail
- Últimas 24 h (o lo que pida): agrupar en **responder hoy** · **puede esperar** · **solo informativo** · **ruido**
  (newsletters, notificaciones). Una línea por correo: quién · qué quiere · qué hay que hacer.
- Para «responder hoy», dejar **borradores** en su tono (con el conector, como borrador en Gmail). **Nunca enviar**,
  archivar ni borrar sin OK explícito.

## Calendario
- Agenda de hoy y mañana con huecos libres. Para cada reunión: con quién, de qué va (buscar el último correo o la nota
  de `~/Desktop/Agentes/reuniones/` de esa persona) y qué llevar preparado.
- «Búscame un hueco»: proponer 2–3 opciones respetando bloques de trabajo; crear el evento solo con OK.

## Avisos
Lista corta, lo más urgente arriba: correos que esperan su respuesta hace > 48 h, reuniones sin preparar, plazos o
pagos que vencen esta semana (si `/agente-finanzas` dejó alertas en `~/Desktop/Agentes/finanzas/`, incluirlas), y
seguimientos de leads pendientes (`~/Desktop/Agentes/setter/`).

Formato «prepárame el día»: 3 prioridades · agenda · correos a responder · avisos. Que se lea en 1 minuto.
