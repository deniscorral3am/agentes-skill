---
name: agente-prospeccion
description: Agente que busca clientes. Encuentra empresas reales que encajan con el cliente ideal del negocio, investiga cada una (web, reseñas, señales de que tienen el problema) y escribe un primer mensaje personalizado. Deja un CSV listo. Úsala cuando digan /agente-prospeccion, «búscame clientes», «encuentra leads», «lista de empresas para prospectar» o «escribe mensajes en frío».
---

# /agente-prospeccion · busca → investiga → escribe

Leer `~/.claude/agentes/perfil.md` (cliente ideal, para quién NO es, oferta, tono, prueba). Preguntar solo lo que falte:
**zona** (ciudad/país) y **cuántas** (por defecto 10). Guardar en `~/Desktop/Agentes/prospeccion/<AAAA-MM-DD>-<nicho>.csv`
con columnas `empresa,web,ciudad,contacto,señal,fuente,mensaje,canal`.

## 1 · Busca
- WebSearch con varias consultas (sector + ciudad, directorios, Google Maps, «mejores <sector> en <ciudad>»).
- Quedarse solo con empresas **reales y activas** (web que carga, reseñas recientes). Descartar las que el perfil dice
  que no encajan. Cada una con su fuente.

## 2 · Investiga (WebFetch de su web y, si se puede, reseñas)
Por empresa, 1 **señal** concreta de que tienen el problema que resuelve la oferta. Ejemplos: no responden reseñas,
formulario sin respuesta automática, sin reservas online, web lenta, anuncios activos sin página de destino, quejas
de «no cogen el teléfono». Si no se encuentra señal, se pone «sin señal» y baja en la lista. Nunca inventarla.

## 3 · Escribe
- Mensaje de ≤ 80 palabras por empresa: la señal concreta → lo que eso les cuesta en una línea → una pregunta fácil de
  contestar. Sin PDF, sin precio, sin «somos una agencia líder».
- Canal recomendado (email, Instagram, LinkedIn, WhatsApp de empresa) según lo que tengan visible.
- Contacto: solo datos públicos de empresa (email o teléfono de la web). No buscar datos personales privados.

Entrega: las 3 mejores con su mensaje en la respuesta y la ruta del CSV. Nunca enviar nada por su cuenta.
