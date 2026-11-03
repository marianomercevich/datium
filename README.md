# DatiumTech — sitio, medición y operación

Sitio estático en **https://datiumtech.com.ar** (Hostinger). Contactos por **Web3Forms** al mail. Visitas y campañas: **GA4** + **Meta Pixel** (solo si el visitante acepta cookies).

## Dónde mirar cada cosa

| Pregunta | Dónde | Qué ves |
|---|---|---|
| ¿Quién entra al sitio? | [Google Analytics 4](https://analytics.google.com/) → propiedad **G-ZTE21X9Q9V** → Informes → Adquisición | Canal (Organic, Paid, Direct, Referral), landing, dispositivo |
| ¿Por qué palabras nos encuentran? | [Search Console](https://search.google.com/search-console) → propiedad `datiumtech.com.ar` | Consultas, clics, impresiones, páginas |
| ¿De qué anuncio de IG/FB viene el lead? | Mail del formulario (campo **canal** / **utm_***) + [Events Manager](https://business.facebook.com/events_manager) Pixel **1927140795342157** | Eventos PageView, Lead, whatsapp_click |
| ¿Llegó un contacto? | Inbox de **datiumtech@gmail.com** (Web3Forms) | Nombre, servicio, pago, **canal**, **landing**, **pagina**, UTM |
| ¿Alguien tocó WhatsApp? | GA4 → Eventos → `whatsapp_click` | Clics al botón / flotante (si aceptó cookies) |

Los contactos **siempre** llegan por mail, aunque la persona rechace cookies. El origen (Google Ads, Meta, orgánico, directo) viaja en el mismo mail.

## Cómo leer un mail de lead

Asunto ejemplo: `Nuevo lead — Datium · meta_ads`

| Campo | Significado |
|---|---|
| `canal` | `google_ads` · `google_organico` · `meta_ads` · `whatsapp` · `directo` · `referral` · `redes` |
| `landing` | Primera URL de esa visita (dónde aterrizó) |
| `pagina` | URL desde la que envió el formulario |
| `referrer` | Sitio anterior, o `(directo)` |
| `utm_source` / `utm_medium` / `utm_campaign` | Campaña (último toque) |
| `gclid` / `fbclid` | Clic de Google Ads o Meta |
| `first_utm_source` | Primera campaña de la sesión |

## Links de campaña (usar siempre UTM)

```
https://datiumtech.com.ar/landing-page/?utm_source=meta&utm_medium=cpc&utm_campaign=landing_mayo
https://datiumtech.com.ar/?utm_source=google&utm_medium=cpc&utm_campaign=brand
https://datiumtech.com.ar/chatbot-whatsapp/?utm_source=instagram&utm_medium=bio&utm_campaign=perfil
```

Convención:

- Meta Ads: `utm_source=meta` `utm_medium=cpc` `utm_campaign=nombre_del_ad`
- Google Ads: activar auto-tagging (`gclid`); opcional los mismos UTM
- Historias / bio: `utm_source=instagram` `utm_medium=bio`
- WhatsApp de campaña: `utm_source=whatsapp` `utm_medium=broadcast`

## Eventos que dispara el sitio

Con cookies aceptadas (`js/consent.js` + `js/track.js`):

| Evento | Cuándo | GA4 | Meta |
|---|---|---|---|
| `page_view` | Cada página | sí | PageView |
| `generate_lead` | Formulario OK | sí | Lead |
| `whatsapp_click` | Clic en wa.me | sí | custom |
| `cta_click` | CTA planes / “Hablar con un asesor” | sí | custom |

## SEO (ya en el sitio)

- Canonical apex `https://datiumtech.com.ar/` (www redirige)
- Sitemap: `/sitemap.xml` — declarado en `robots.txt`
- Schema: ProfessionalService + Offer (ARS) + FAQ
- Páginas de servicio indexables: `/landing-page/`, `/sitio-web/`, `/chatbot-whatsapp/`, `/apps-moviles/`, `/automatizaciones/`, `/seo/`, `/ecommerce/`, `/servicios/`
- OG image: `/og-image.jpg` (1200×630)

Pendiente en Search Console (una vez):

1. Verificar la propiedad **sin www** si no está.
2. Enviar sitemap `https://datiumtech.com.ar/sitemap.xml`.
3. Inspeccionar las URLs de servicio nuevas.

## Panel local de métricas

No va a Hostinger. En tu PC:

```
cd panel
python -m pip install -r requirements.txt
python app.py
```

Abrí http://127.0.0.1:8788/ — la clave se imprime en la terminal (queda en `panel/.env`).

Sin `credentials.json` ves los accesos a GA4, Search Console, Meta y Web3Forms. Con una cuenta de servicio de Google, el mismo panel trae usuarios, canales, landings, leads, WhatsApp y consultas.

## Hosting y deploy

Hostinger, cuenta FTP del sitio DatiumTech. Carpeta remota: `public_html`.

Subir, como mínimo: `index.html`, `privacidad.html`, `robots.txt`, `sitemap.xml`, `favicon.svg`, `og-image.jpg`, `css/`, `js/`, y las carpetas de servicio.

No hace falta base de datos.

Regenerar landings de servicio:

```
python tools/gen_servicios.py
```

## Formulario

Web3Forms, access key ya cargada. Límite free ~250 envíos/mes. Restringir la key al dominio `datiumtech.com.ar` en el panel de Web3Forms.

WhatsApp: **+54 9 11 7652-2232** (`wa.me/5491176522232`).

DatiumTech — datiumtech@gmail.com — +54 9 11 7652-2232
