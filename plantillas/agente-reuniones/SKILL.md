---
name: agente-reuniones
description: Agente que resume reuniones. Lee la transcripción o grabación de una llamada (Fathom, Fireflies, Zoom, Meet, audio), saca decisiones, dolores, objeciones y próximos pasos, y escribe el email de seguimiento. Úsala cuando digan /agente-reuniones, «resume esta llamada», «qué se dijo en la reunión», «hazme el seguimiento» o pasen una transcripción.
---

# /agente-reuniones · escucha → resume → seguimiento

Leer `~/.claude/agentes/perfil.md` (oferta, tono, enlace de calendario). Guardar en
`~/Desktop/Agentes/reuniones/<AAAA-MM-DD>-<con quién>.md`.

## 1 · Escucha
Fuentes, de mejor a peor:
- Transcripción en texto (`.txt`, `.vtt`, `.srt`, `.docx`, copiar/pegar de Fathom, Fireflies, Zoom o Meet).
- Grabación de audio/vídeo: si hay `whisper` o `faster-whisper` instalado, transcribir en local; si no, pedir la
  transcripción que da su herramienta de grabación. No subir la grabación a ningún sitio sin permiso.
Identificar quién habla (nosotros / el cliente) aunque la transcripción no lo marque.

## 2 · Resume
Con esta estructura, citando frases literales del cliente cuando importan:
- **En una línea**: qué pasó y cómo quedó.
- **Su situación y su dolor**, en sus palabras.
- **Lo que quiere conseguir** y para cuándo.
- **Objeciones o dudas** que salieron y si quedaron resueltas.
- **Decisiones** tomadas.
- **Próximos pasos**: quién · qué · cuándo.
- **Temperatura**: caliente / tibio / frío, con el porqué.
Si es una llamada de venta, añadir qué se hizo bien y la pregunta que faltó hacer.

## 3 · Seguimiento
- Email o mensaje de seguimiento listo para copiar: agradece, resume en 3 puntos lo acordado con sus palabras, deja
  el siguiente paso con fecha. Corto y en el tono del perfil.
- Lista de tareas para nosotros.
Nunca enviarlo solo, y nunca añadir compromisos que no se dijeron en la llamada.
