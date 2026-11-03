# -*- coding: utf-8 -*-
"""Genera css/site.css y las landings de servicio."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
css_match = re.search(r"<style>(.*?)</style>", INDEX, re.S)
if not css_match:
    raise SystemExit("No encontré el bloque <style> en index.html")

EXTRA_CSS = """
.svc-card{text-decoration:none;color:inherit;display:block;cursor:pointer}
.svc-card .svc-more{
  display:inline-block;margin-top:1rem;
  font-size:.8rem;font-weight:700;color:var(--cyan)
}
.page-hero{
  padding:8.5rem 2rem 3.5rem;position:relative;overflow:hidden
}
.page-hero .hero-grid,.page-hero .hero-glow{position:absolute;inset:0}
.page-hero-inner{max-width:1100px;margin:0 auto;position:relative}
.crumbs{display:flex;flex-wrap:wrap;gap:.4rem;font-size:.78rem;color:var(--tx3);margin-bottom:1.4rem}
nav.crumbs{position:static;inset:auto;top:auto;left:auto;right:auto;height:auto;width:auto;padding:0;background:none;border:0;box-shadow:none;backdrop-filter:none;-webkit-backdrop-filter:none;z-index:auto;justify-content:flex-start;align-items:center}
.crumbs a{color:var(--tx3);text-decoration:none}
.crumbs a:hover{color:var(--cyan)}
.page-h1{
  font-family:'Barlow Condensed',sans-serif;
  font-size:clamp(2.4rem,5vw,4.2rem);font-weight:900;line-height:1;
  margin-bottom:1rem
}
.page-lead{color:var(--tx2);font-size:1.05rem;line-height:1.75;max-width:680px;margin-bottom:2rem}
.page-meta{display:flex;flex-wrap:wrap;gap:1rem;margin-bottom:2rem}
.page-chip{
  border:1px solid var(--brd-c);background:var(--cyan-dim);
  color:var(--cyan);padding:.4rem .85rem;border-radius:6px;font-size:.78rem;font-weight:700
}
.prose{color:var(--tx2);font-size:.98rem;line-height:1.75;max-width:720px}
.prose p{margin-bottom:1rem}
.prose h2{
  font-family:'Barlow Condensed',sans-serif;font-size:1.8rem;font-weight:800;
  color:var(--tx);margin:2.2rem 0 .8rem
}
.prose ul{list-style:none;margin:0 0 1.2rem}
.prose ul li{padding:.28rem 0 .28rem 1.3rem;position:relative}
.prose ul li::before{content:'→';color:var(--cyan);position:absolute;left:0}
.faq details{
  border:1px solid var(--brd);border-radius:10px;padding:1rem 1.2rem;margin-bottom:.7rem;
  background:var(--card)
}
.faq summary{
  font-family:'Barlow Condensed',sans-serif;font-weight:800;cursor:pointer;color:var(--tx)
}
.faq details p{margin:.7rem 0 0;color:var(--tx2);font-size:.9rem;line-height:1.65}
.related{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;margin-top:1.2rem}
.related a{
  display:block;padding:1.2rem;border:1px solid var(--brd);border-radius:12px;
  text-decoration:none;color:var(--tx2);background:var(--card)
}
.related a:hover{border-color:var(--brd-c);color:var(--tx)}
.related strong{display:block;color:var(--tx);margin-bottom:.35rem}
form.contact-form{background:var(--bg2);border:1px solid var(--brd);border-radius:16px;padding:2.5rem}
.brand-kicker{
  display:block;font-family:'Barlow Condensed',sans-serif;font-size:clamp(1.1rem,2vw,1.35rem);
  font-weight:800;letter-spacing:.14em;color:var(--cyan);margin-bottom:.6rem
}
#form-msg,.form-msg{display:none;margin-top:1rem;padding:.9rem 1.2rem;border-radius:8px;font-size:.85rem;font-weight:500;text-align:center}
#form-msg.ok,.form-msg.ok{display:block;background:rgba(0,229,255,.1);color:var(--cyan);border:1px solid var(--cyan-brd)}
#form-msg.err,.form-msg.err{display:block;background:rgba(255,61,0,.12);color:#ff8a70;border:1px solid rgba(255,61,0,.35)}
"""

(ROOT / "css").mkdir(exist_ok=True)
(ROOT / "css" / "site.css").write_text(css_match.group(1).strip() + "\n" + EXTRA_CSS, encoding="utf-8")

SERVICES = [
    {
        "slug": "landing-page",
        "nav": "Landing page",
        "h1": "Landing page profesional en Argentina",
        "title": "Landing page Argentina | DatiumTech",
        "description": "Landing page a medida desde $350.000. Diseño único, SEO, WhatsApp y entrega en 7 días. DatiumTech — Argentina y LATAM.",
        "price": "desde $350.000 (~USD 250)",
        "option": "Landing Page — Promo $350.000",
        "wa": "Hola%20DatiumTech%2C%20quiero%20una%20landing%20page",
        "chips": ["7 días de entrega", "SEO on-page", "Mobile first"],
        "intro": "Una landing page bien hecha es la diferencia entre una campaña que quema plata y una que trae clientes. En DatiumTech diseñamos landing pages para negocios de Argentina y LATAM: una sola página, un solo objetivo, copy claro y formulario que llega.",
        "body": """
<p>Si estás por invertir en Meta Ads o Google Ads, necesitás una URL que convierta. No un sitio genérico con diez menús. Una <strong>landing page profesional</strong> enfocada en un servicio, un turno o un pedido.</p>
<p>Trabajamos a medida: no usamos plantillas recicladas. Entregamos en 7 días hábiles, con versión mobile, WhatsApp, SEO básico y formulario funcional.</p>
<h2>Qué incluye la landing page</h2>
<ul>
<li>Diseño único alineado a tu marca</li>
<li>Copy orientado a conversión (no relleno)</li>
<li>Formulario + botón de WhatsApp</li>
<li>Adaptación a celular y tablet</li>
<li>SEO on-page: título, description, headings y velocidad</li>
<li>Pixel de Meta y medición lista para campañas</li>
</ul>
<h2>Para quién es</h2>
<p>Consultorios, estudios, comercios, infoproductos, inmobiliarias y cualquier negocio que necesite captar leads rápido sin armar un sitio de 8 páginas.</p>
""",
        "faqs": [
            ("¿Cuánto cuesta una landing page profesional?", "La promo de lanzamiento arranca en $350.000 ARS (aprox. USD 250). Precio fijo, sin sorpresas."),
            ("¿En cuánto tiempo la entregan?", "7 días hábiles desde que cerramos textos, fotos y el objetivo de la página."),
            ("¿Sirve para anuncios de Instagram y Google?", "Sí. La armamos para campañas: un mensaje, un CTA y tracking (Pixel / Analytics)."),
            ("¿Se puede financiar?", "Sí. Contado, 3 cuotas sin interés, o 6/12 cuotas a convenir. También armamos un plan a medida."),
        ],
        "related": ["sitio-web", "chatbot-whatsapp", "seo"],
    },
    {
        "slug": "sitio-web",
        "nav": "Sitio web",
        "h1": "Sitio web corporativo para empresas",
        "title": "Sitio web corporativo | DatiumTech",
        "description": "Sitio web profesional con hasta 8 secciones, panel de edición y hosting. Desde $850.000. DatiumTech en Argentina.",
        "price": "desde $850.000 (~USD 600)",
        "option": "Sitio Web Corporativo",
        "wa": "Hola%20DatiumTech%2C%20quiero%20un%20sitio%20web",
        "chips": ["Hasta 8 secciones", "Panel admin", "Hosting 1er año"],
        "intro": "Tu empresa necesita más que una tarjeta digital. Un sitio web corporativo explica quién sos, qué vendés y por qué confiar. DatiumTech lo construye con estructura clara, rápido y administrable.",
        "body": """
<p>Diseñamos sitios institucionales para pymes de Argentina, México, Chile y el resto de LATAM. Home, servicios, nosotros, blog o casos, contacto — sin plantillas genéricas.</p>
<h2>Qué incluye</h2>
<ul>
<li>Hasta 8 secciones o páginas</li>
<li>Panel para editar textos e imágenes</li>
<li>Dominio + hosting el primer año (si lo contratás con nosotros)</li>
<li>Formulario de contacto con aviso por email</li>
<li>Base SEO: URLs limpias, metadatos y sitemap</li>
</ul>
<h2>Por qué no alcanza con una landing</h2>
<p>La landing cierra una campaña. El sitio web es tu casa digital: credibilidad, SEO de marca y un lugar donde el cliente vuelve. Si Google todavía no te encuentra por el nombre de tu empresa, acá se empieza.</p>
""",
        "faqs": [
            ("¿Puedo editar el sitio yo después?", "Sí. Incluimos panel de administración y una capacitación corta."),
            ("¿El precio incluye hosting?", "El primer año de hosting y dominio puede ir incluido. Lo vemos en la propuesta."),
            ("¿Hacen sitios en WordPress?", "Usamos la stack que mejor se adapte al proyecto. Lo importante es que vos puedas actualizar contenido."),
        ],
        "related": ["landing-page", "seo", "ecommerce"],
    },
    {
        "slug": "chatbot-whatsapp",
        "nav": "Chatbot WhatsApp",
        "h1": "Chatbot con IA para WhatsApp",
        "title": "Chatbot WhatsApp con IA | DatiumTech",
        "description": "Chatbot con IA para WhatsApp, Instagram y web. Califica leads y responde 24/7. Desde $480.000. DatiumTech.",
        "price": "desde $480.000 (~USD 350)",
        "option": "Chatbot con IA",
        "wa": "Hola%20DatiumTech%2C%20quiero%20un%20chatbot%20para%20WhatsApp",
        "chips": ["WhatsApp + Instagram", "IA entrenada", "24/7"],
        "intro": "El 80% de tus consultas llegan fuera de horario o se enfrían en el inbox. Un chatbot con IA en WhatsApp responde al toque, califica al lead y te avisa solo cuando hay una oportunidad real.",
        "body": """
<p>En DatiumTech entrenamos el bot con tu negocio: precios, FAQs, zonas, turnos. Se integra a WhatsApp, Instagram y la web. No es un menú rígido de “presioná 1”: entiende lenguaje natural.</p>
<h2>Qué incluye</h2>
<ul>
<li>IA entrenada con tu catálogo y tono de marca</li>
<li>WhatsApp Business, Instagram y widget web</li>
<li>Calificación automática de leads</li>
<li>Panel de control y métricas</li>
<li>Handoff a un humano cuando hace falta</li>
</ul>
<h2>Resultado típico</h2>
<p>Menos tiempo en copiar y pegar la misma respuesta. Más turnos o ventas tomados de noche y el finde. El bot no reemplaza a tu equipo: le saca el trabajo repetido.</p>
""",
        "faqs": [
            ("¿Funciona con el WhatsApp que ya uso?", "Sí. Lo conectamos a WhatsApp Business. Coordinamos el número en la llamada de arranque."),
            ("¿Se entrena con mi información?", "Sí. Cargamos FAQs, precios y objeciones. Lo vamos ajustando las primeras semanas."),
            ("¿Puede agendar reuniones?", "Sí, si tu calendario lo permite (Google Calendar u otra agenda que definamos)."),
        ],
        "related": ["automatizaciones", "landing-page", "apps-moviles"],
    },
    {
        "slug": "apps-moviles",
        "nav": "Apps móviles",
        "h1": "Apps móviles iOS y Android",
        "title": "App móvil iOS y Android | DatiumTech",
        "description": "Desarrollo de apps móviles iOS y Android con React Native. MVP desde USD 3.500. DatiumTech, Argentina y LATAM.",
        "price": "desde USD 3.500",
        "option": "App Móvil",
        "wa": "Hola%20DatiumTech%2C%20quiero%20una%20app%20móvil",
        "chips": ["iOS + Android", "React Native", "MVP rápido"],
        "intro": "Una app tiene sentido cuando tu cliente vuelve: pedidos, turnos, comunidad, campo o un interno de la empresa. DatiumTech desarrolla iOS y Android con una sola base (React Native) para no pagar dos veces.",
        "body": """
<p>Arrancamos por un MVP: lo mínimo para validar. Panel de administración, notificaciones push y pagos con MercadoPago si vendés desde la app.</p>
<h2>Qué incluye</h2>
<ul>
<li>App iOS y Android</li>
<li>Panel admin</li>
<li>Push notifications</li>
<li>Integración de pagos (MercadoPago / Stripe según mercado)</li>
<li>Publicación en stores (te acompañamos en las cuentas de desarrollador)</li>
</ul>
<h2>Cuándo NO hacer una app</h2>
<p>Si todavía no tenés demanda ni un flujo claro, una landing o un PWA puede alcanzar. Te lo decimos en la primera llamada: no vendemos app por vender app.</p>
""",
        "faqs": [
            ("¿Cuánto tarda un MVP?", "Depende del alcance. Un MVP acotado suele llevar varias semanas, no meses eternos."),
            ("¿Queda el código para nosotros?", "Sí. El producto es tuyo. Lo acordamos en contrato."),
            ("¿Sirve para Argentina y el exterior?", "Sí. Podemos publicar en ambos stores y adaptar pagos por país."),
        ],
        "related": ["automatizaciones", "sitio-web", "chatbot-whatsapp"],
    },
    {
        "slug": "automatizaciones",
        "nav": "Automatizaciones",
        "h1": "Automatizaciones y CRM a medida",
        "title": "Automatizaciones y CRM | DatiumTech",
        "description": "Automatizá ventas, WhatsApp y reportes. CRM a medida desde $680.000. DatiumTech — Make, APIs y paneles propios.",
        "price": "desde $680.000 (~USD 500)",
        "option": "Automatizaciones y CRM",
        "wa": "Hola%20DatiumTech%2C%20quiero%20automatizar%20mi%20negocio",
        "chips": ["CRM a medida", "WhatsApp API", "Menos trabajo manual"],
        "intro": "Si tu equipo copia datos de WhatsApp a una planilla, se te escapan leads. Automatizamos ese flujo: CRM, recordatorios, reportes y el puente con las herramientas que ya usás.",
        "body": """
<p>Integramos Make, APIs, WhatsApp Business y paneles propios. El objetivo no es “tener un CRM famoso”: es que tu operación deje de depender de memoria y Excel.</p>
<h2>Qué automatizamos</h2>
<ul>
<li>Captura de leads desde web y anuncios hacia un CRM</li>
<li>Seguimiento y recordatorios</li>
<li>Mensajes de WhatsApp con plantillas y bots</li>
<li>Reportes diarios o semanales</li>
<li>Sincronización con MercadoPago, calendarios y mail</li>
</ul>
""",
        "faqs": [
            ("¿Reemplazan HubSpot o es algo propio?", "Puede ser CRM a medida o integrar el que ya tenés. Lo definimos según volumen y presupuesto."),
            ("¿Hace falta saber programar para usarlo?", "No. El día a día es un panel o las apps que ya usan (WhatsApp, mail)."),
            ("¿Cuánto tarda?", "Un flujo acotado puede salir en días. Un CRM completo se arma por etapas."),
        ],
        "related": ["chatbot-whatsapp", "apps-moviles", "seo"],
    },
    {
        "slug": "seo",
        "nav": "SEO",
        "h1": "SEO y posicionamiento en Google",
        "title": "SEO y posicionamiento | DatiumTech",
        "description": "SEO para negocios de Argentina y LATAM: técnico, contenidos y medición. Desde $280.000/mes. DatiumTech.",
        "price": "desde $280.000/mes (~USD 200)",
        "option": "SEO y Posicionamiento",
        "wa": "Hola%20DatiumTech%2C%20quiero%20mejorar%20mi%20SEO",
        "chips": ["SEO técnico", "Keywords locales", "Reporte mensual"],
        "intro": "Si nadie busca tu marca, Google no te va a regalar tráfico. El SEO de DatiumTech arranca por lo técnico (indexación, velocidad, URLs) y sigue con páginas que responden búsquedas reales: “landing page”, “chatbot WhatsApp”, el nombre de tu servicio + ciudad.",
        "body": """
<p>Search Console no miente: sin páginas de servicio y sin marca consolidada, un sitio no aparece. Por eso combinamos auditoría, contenido y enlaces con sentido (no granjas).</p>
<h2>Qué incluye el plan mensual</h2>
<ul>
<li>Auditoría técnica</li>
<li>Arquitectura de páginas y keywords</li>
<li>Optimización on-page</li>
<li>Link building local/nacional con criterio</li>
<li>Reporte de posiciones e impresiones</li>
</ul>
<p>El SEO no es magia de 7 días. En 60–90 días se ve si las impresiones de marca suben y si aparecen las primeras consultas de servicio.</p>
""",
        "faqs": [
            ("¿Garantizan el puesto 1?", "Nadie serio lo garantiza. Sí medimos impresiones, clics y posiciones y priorizamos quick wins (marca + fichas)."),
            ("¿Sirve si recién lanzo el sitio?", "Sí. El mejor momento para SEO técnico es ahora: sitemap, HTTPS, páginas de servicio e indexación."),
            ("¿Trabajan Argentina nada más?", "El foco es Argentina y LATAM. España y otros países se evalúan por competencia."),
        ],
        "related": ["landing-page", "sitio-web", "ecommerce"],
    },
    {
        "slug": "ecommerce",
        "nav": "E-commerce",
        "h1": "Tienda online y e-commerce",
        "title": "E-commerce y tienda online | DatiumTech",
        "description": "Tienda online con MercadoPago, catálogo y stock. Desde $1.500.000. DatiumTech, Argentina.",
        "price": "desde $1.500.000 (~USD 1.000)",
        "option": "E-commerce",
        "wa": "Hola%20DatiumTech%2C%20quiero%20una%20tienda%20online",
        "chips": ["MercadoPago", "Catálogo y stock", "Checkout claro"],
        "intro": "Una tienda online que no cobra en MercadoPago o que se cae en el celular no vende. Armamos e-commerce para marcas que necesitan catálogo, carrito, medios de pago locales y un panel de pedidos entendible.",
        "body": """
<p>Integramos MercadoPago, tarjetas y transferencia. Gestión de stock y pedidos. Si además vendés afuera, vemos Stripe u otro medio.</p>
<h2>Qué incluye</h2>
<ul>
<li>Catálogo (escalable)</li>
<li>Carrito y checkout</li>
<li>MercadoPago + tarjetas + transferencia</li>
<li>Panel de pedidos y stock</li>
<li>Base para Instagram Shopping / catálogo, si aplica</li>
</ul>
""",
        "faqs": [
            ("¿Es Shopify o a medida?", "Elegimos según catálogo, presupuesto y si necesitás algo muy custom. Te lo decimos en la propuesta."),
            ("¿Puedo cargar productos yo?", "Sí. El panel está pensado para que tu equipo cargue fotos, precios y stock."),
            ("¿Hacen envíos y facturación?", "Integramos lo que uses (correo, OCA, facturadores). Se cotiza según el stack."),
        ],
        "related": ["sitio-web", "automatizaciones", "seo"],
    },
]

BY_SLUG = {s["slug"]: s for s in SERVICES}

HEAD = """<!DOCTYPE html>
<html lang="es-419">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{description}">
<title>{title}</title>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="author" content="DatiumTech">
<meta name="theme-color" content="#080B14">
<link rel="canonical" href="https://datiumtech.com.ar/{slug}/">
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<meta property="og:type" content="website">
<meta property="og:site_name" content="DatiumTech">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://datiumtech.com.ar/{slug}/">
<meta property="og:image" content="https://datiumtech.com.ar/og-image.jpg">
<meta property="og:locale" content="es_419">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://datiumtech.com.ar/og-image.jpg">
<script type="application/ld+json">{schema}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap"></noscript>
<link rel="stylesheet" href="../css/site.css">
</head>
"""

NAV = """<nav>
  <a href="../" class="logo" style="display:flex;align-items:center;gap:10px;text-decoration:none">
    <span style="color:var(--tx)">DATIUM<span style="color:var(--cyan)">TECH</span></span>
  </a>
  <div class="nav-links">
    <a href="../servicios/">Servicios</a>
    <a href="../blog/">Blog</a>
    <a href="../#planes">Planes</a>
    <a href="#contacto">Contacto</a>
  </div>
  <a href="#contacto" class="nav-cta">Hablar con un asesor</a>
  <button type="button" class="nav-menu" id="nav-toggle" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
</nav>
"""

WA_ICON = """<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>"""


def schema_for(s):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://datiumtech.com.ar/"},
                    {"@type": "ListItem", "position": 2, "name": s["nav"], "item": f"https://datiumtech.com.ar/{s['slug']}/"},
                ],
            },
            {
                "@type": "Service",
                "name": s["h1"],
                "provider": {"@type": "ProfessionalService", "name": "DatiumTech", "url": "https://datiumtech.com.ar"},
                "areaServed": ["AR", "MX", "CL", "CO", "UY", "PE"],
                "description": s["description"],
                "url": f"https://datiumtech.com.ar/{s['slug']}/",
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in s["faqs"]
                ],
            },
        ],
    }


def options_html(selected):
    opts = [
        "Landing Page — Promo $350.000",
        "Sitio Web Corporativo",
        "App Móvil",
        "Automatizaciones y CRM",
        "Chatbot con IA",
        "SEO y Posicionamiento",
        "E-commerce",
        "Consultoría Digital",
        "Plan a medida",
        "Otro / No sé por dónde empezar",
    ]
    out = []
    for o in opts:
        sel = " selected" if o == selected else ""
        out.append(f'<option{sel}>{o}</option>')
    return "\n            ".join(out)


def page_html(s):
    related = []
    for slug in s["related"]:
        o = BY_SLUG[slug]
        related.append(f'<a href="../{o["slug"]}/"><strong>{o["nav"]}</strong>{o["price"]}</a>')
    faqs = []
    for q, a in s["faqs"]:
        faqs.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    chips = "".join(f'<span class="page-chip">{c}</span>' for c in s["chips"])
    schema = json.dumps(schema_for(s), ensure_ascii=False, separators=(",", ":"))
    return f"""{HEAD.format(description=s['description'], title=s['title'], slug=s['slug'], schema=schema)}
<body>
{NAV}
<section class="page-hero">
  <div class="hero-glow"></div>
  <div class="hero-grid"></div>
  <div class="page-hero-inner">
    <nav class="crumbs" aria-label="Miga de pan">
      <a href="../">Inicio</a> <span>/</span> <a href="../#servicios">Servicios</a> <span>/</span> <span>{s['nav']}</span>
    </nav>
    <p class="brand-kicker">DATIUMTECH</p>
    <h1 class="page-h1">{s['h1']}</h1>
    <p class="page-lead">{s['intro']}</p>
    <div class="page-meta">{chips}<span class="page-chip">{s['price']}</span></div>
    <div class="hero-actions">
      <a href="#contacto" class="btn-main">Pedir propuesta</a>
      <a class="btn-wa" href="https://wa.me/5491176522232?text={s['wa']}" target="_blank" rel="noopener noreferrer">{WA_ICON} WhatsApp</a>
    </div>
  </div>
</section>
<section>
  <div class="section-inner prose">
    {s['body']}
    <h2>Preguntas frecuentes</h2>
    <div class="faq">{''.join(faqs)}</div>
    <h2>Otros servicios DatiumTech</h2>
    <div class="related">{''.join(related)}</div>
  </div>
</section>
<section id="contacto">
  <div class="section-inner">
    <div class="contact-wrap">
      <div class="contact-left">
        <div class="section-eyebrow">Hablemos</div>
        <h2>PEDÍ TU<br><span class="highlight">PROPUESTA</span></h2>
        <p>DatiumTech te responde en horario laboral. Contado, 3 cuotas s/interés o plan a medida.</p>
      </div>
      <form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="b86ff358-3ebe-49d6-969a-8ad4c356ee51">
        <input type="hidden" name="subject" value="Lead {s['nav']} — DatiumTech">
        <input type="hidden" name="from_name" value="Datium Web">
        <input class="hp" type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="form-row">
          <div class="fg"><label for="nombre">Nombre *</label><input id="nombre" name="nombre" required></div>
          <div class="fg"><label for="apellido">Apellido *</label><input id="apellido" name="apellido" required></div>
        </div>
        <div class="fg"><label for="email-f">Email *</label><input id="email-f" type="email" name="email" required></div>
        <div class="fg"><label for="telefono">WhatsApp</label><input id="telefono" type="tel" name="telefono" placeholder="+54 9 11 7652-2232"></div>
        <div class="fg">
          <label for="servicio">Servicio *</label>
          <select id="servicio" name="servicio" required>
            {options_html(s['option'])}
          </select>
        </div>
        <div class="fg">
          <label for="pago">Forma de pago</label>
          <select id="pago" name="pago">
            <option value="" selected>A convenir</option>
            <option>Contado</option>
            <option>3 cuotas sin interés</option>
            <option>6 cuotas</option>
            <option>12 cuotas / financiación a medida</option>
          </select>
        </div>
        <div class="fg"><label for="mensaje">Proyecto</label><textarea id="mensaje" name="mensaje"></textarea></div>
        <div class="prv">
          <input type="checkbox" id="prv" name="privacy" required>
          <label for="prv">Acepto la <a href="../privacidad.html">política de privacidad</a>.</label>
        </div>
        <button class="form-submit" type="submit">QUIERO QUE ME CONTACTEN →</button>
        <div class="form-msg" role="status"></div>
      </form>
    </div>
  </div>
</section>
<footer>
  <div class="footer-inner">
    <div class="footer-logo">DATIUM<span>TECH</span></div>
    <div class="footer-copy">© 2026 DatiumTech</div>
    <div class="footer-links">
      <a href="../">Inicio</a>
      <a href="../#planes">Planes</a>
      <a href="../servicios/">Servicios</a>
      <a href="../blog/">Blog</a>
      <a href="../privacidad.html">Privacidad</a>
    </div>
  </div>
</footer>
<script>
const navToggle=document.getElementById('nav-toggle');
const navLinks=document.querySelector('.nav-links');
if(navToggle&&navLinks){{
  navToggle.addEventListener('click',()=>{{
    const open=navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open?'true':'false');
  }});
}}
</script>
<script src="../js/consent.js" defer></script>
<script src="../js/track.js" defer></script>
<div id="cookie-bar" class="cookie-bar" role="dialog" aria-label="Cookies">
  <p>Usamos cookies de Analytics y Meta Pixel si las aceptás. Detalle en la <a href="../privacidad.html">política de privacidad</a>.</p>
  <div class="cookie-actions">
    <button type="button" id="cookie-no">Solo esenciales</button>
    <button type="button" id="cookie-ok">Aceptar</button>
  </div>
</div>
</body>
</html>
"""


for s in SERVICES:
    d = ROOT / s["slug"]
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page_html(s), encoding="utf-8")

# Hub
cards = []
for s in SERVICES:
    cards.append(
        f'<a class="svc-card" href="../{s["slug"]}/"><h3>{s["nav"]}</h3><p>{s["intro"][:140]}…</p><div class="svc-price">{s["price"]}</div><span class="svc-more">Ver servicio →</span></a>'
    )

hub = f"""<!DOCTYPE html>
<html lang="es-419">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Servicios DatiumTech | Landing, apps, chatbots y SEO</title>
<meta name="description" content="Servicios de DatiumTech: landing pages, sitios web, chatbots WhatsApp, apps, automatizaciones, SEO y e-commerce para Argentina y LATAM.">
<link rel="canonical" href="https://datiumtech.com.ar/servicios/">
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<meta property="og:title" content="Servicios DatiumTech | Landing, apps, chatbots y SEO">
<meta property="og:description" content="Landing pages, sitios, apps, chatbots con IA, CRM y SEO. Precio fijo. Argentina y LATAM.">
<meta property="og:url" content="https://datiumtech.com.ar/servicios/">
<meta property="og:image" content="https://datiumtech.com.ar/og-image.jpg">
<link rel="stylesheet" href="../css/site.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">
</head>
<body>
{NAV}
<section class="page-hero">
  <div class="page-hero-inner">
    <p class="brand-kicker">DATIUMTECH</p>
    <h1 class="page-h1">Servicios de desarrollo y automatización</h1>
    <p class="page-lead">Landing pages, sitios, apps, chatbots con IA, CRM y SEO. Precio fijo. Contado, cuotas o plan a medida. Argentina y LATAM.</p>
  </div>
</section>
<section id="servicios">
  <div class="section-inner">
    <div class="services-grid">{''.join(cards)}</div>
  </div>
</section>
<footer>
  <div class="footer-inner">
    <div class="footer-logo">DATIUM<span>TECH</span></div>
    <div class="footer-links"><a href="../">Inicio</a><a href="../#planes">Planes</a><a href="../privacidad.html">Privacidad</a></div>
  </div>
</footer>
<script>
const navToggle=document.getElementById('nav-toggle');
const navLinks=document.querySelector('.nav-links');
if(navToggle&&navLinks){{
  navToggle.addEventListener('click',()=>{{
    const open=navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open?'true':'false');
  }});
}}
</script>
<script src="../js/consent.js" defer></script>
<script src="../js/track.js" defer></script>
<div id="cookie-bar" class="cookie-bar" role="dialog" aria-label="Cookies">
  <p>Usamos cookies de Analytics y Meta Pixel si las aceptás. Detalle en la <a href="../privacidad.html">política de privacidad</a>.</p>
  <div class="cookie-actions">
    <button type="button" id="cookie-no">Solo esenciales</button>
    <button type="button" id="cookie-ok">Aceptar</button>
  </div>
</div>
</body>
</html>
"""
hub_dir = ROOT / "servicios"
hub_dir.mkdir(exist_ok=True)
(hub_dir / "index.html").write_text(hub, encoding="utf-8")
print("OK", len(SERVICES), "servicios + hub + css")
