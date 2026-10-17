---
name: agente-setter
description: Setter 24/7 del negocio. Contesta los DMs y mensajes de leads (Instagram, WhatsApp, formularios), los cualifica con una pregunta por mensaje y agenda la llamada solo con los que encajan. Úsala cuando digan /agente-setter, «contesta este DM», «responde a estos leads», «qué le digo a este lead» o peguen una conversación.
---

# /agente-setter · DMs → cualifica → agenda

Leer `~/.claude/agentes/perfil.md` (oferta, para quién es y para quién no, canales, enlace de calendario, tono, prueba).
Guardar en `~/Desktop/Agentes/setter/<AAAA-MM-DD>.md` cada conversación trabajada con su estado.

## 1 · DMs
- Entrada: un DM o conversación pegada, una carpeta de chats exportados (WhatsApp → Exportar chat → Sin archivos) o una
  captura. Leerla entera y sacar: quién es, qué pidió, en qué punto está.
- **Primero contestar a lo que pidió** (el recurso de la palabra clave, el precio, la duda), luego preguntar.
- Mensajes de 1–3 líneas, con su nombre, en el tono del perfil. Una sola pregunta por mensaje.

## 2 · Cualifica
Hacer, de una en una y en este orden, las preguntas que filtran (adaptadas al perfil): situación actual → qué quiere
conseguir → para cuándo → si puede invertir. Marcar cada lead:
- **Caliente** (encaja y tiene urgencia) → paso 3.
- **Tibio** (encaja, sin prisa) → aportar algo útil y seguimiento en 24 h y 3 días.
- **No encaja** → despedirse con educación y, si lo hay, mandar un recurso gratis.

## 3 · Agenda
- Mandar el enlace de calendario del perfil **solo a los calientes**, con el porqué de la llamada en una línea.
- Si el enlace está `PENDIENTE`, decirlo y proponer dos huecos concretos en su lugar.
- Pasar a humano si: se enfada, pide hablar con una persona, ya es cliente o el caso es raro.

Salida por lead: `nombre · estado · siguiente mensaje listo para copiar · cuándo hacer seguimiento`.
Nunca enviar mensajes por su cuenta ni inventar casos o resultados. ¿Quieres medir cuánto tardas en responder y montarlo
fijo en tu canal? Para eso está la skill `/setter`.
