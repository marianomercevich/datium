
DATIUMTECH
Guía de Lanzamiento y Configuración Técnica
Versión 1.0 — Abril 2025


1. Archivos del Proyecto
El sitio está compuesto por los siguientes archivos. Subí todos al mismo directorio raíz del hosting:

index.html	Sitio principal — toda la landing de DatiumTech
privacidad.html	Página de política de privacidad
README.txt	Este documento en formato texto plano

2. Activar el Formulario de Contacto
El formulario usa Web3Forms — gratuito, sin PHP, funciona en cualquier hosting incluido Squarespace.

Paso a paso:
1.	Ir a web3forms.com → clic en 'Get your Access Key'
2.	Ingresar: info@datiumtech.com.ar
3.	Confirmar el email que te envían (importante)
4.	Copiar el Access Key generado (formato: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
5.	Abrir index.html en un editor de texto
6.	Buscar: YOUR_WEB3FORMS_KEY
7.	Reemplazar con tu key real → guardar → subir

Límite gratuito: 250 envíos/mes. Plan de pago desde USD 9/mes sin límite.
¿No llegás a 250 leads por mes? El gratuito es suficiente para empezar.
3. Instalar el Pixel de Meta
El Pixel permite trackear cuántos leads vienen de tus anuncios de Facebook/Instagram. CRÍTICO para optimizar campañas.

Cómo obtener tu Pixel ID:
8.	Ir a business.facebook.com
9.	Events Manager → Conectar fuentes de datos → Web
10.	Elegir 'Pixel de Meta' → dar nombre (ej: DatiumTech Pixel)
11.	Copiar el Pixel ID (número de 15-16 dígitos)

Dónde insertarlo en index.html:
Buscar el comentario <!-- META PIXEL --> antes del cierre </head>. Si no está, agregarlo ahí. Reemplazar XXXXXXXXXXX con tu Pixel ID real:

<script> fbq("init","XXXXXXXXXXX"); fbq("track","PageView"); </script>

Eventos configurados para trackear automáticamente en el formulario:
•	Lead — cuando el formulario se envía correctamente
•	ViewContent — al visitar la página
4. Opciones de Hosting
El sitio es un HTML estático — funciona en prácticamente cualquier hosting. Recomendaciones:

Vercel (recomendado)	Gratis, deploy en 30 segundos, dominio .vercel.app incluido. Conectás GitHub y actualiza automático.
Netlify	Similar a Vercel. Drag & drop del HTML directo en la interfaz. Muy fácil para empezar.
Squarespace	Si ya tenés cuenta, usás Code Injection. Sin PHP nativo pero el formulario Web3Forms funciona.
cPanel/Hostinger	Subís por FTP. Funciona todo. Si querés el contact.php con PHP, acá sí corre.

Deploy en Vercel (más rápido):
12.	Crear cuenta en vercel.com
13.	Arrastrar la carpeta del proyecto a vercel.com/new
14.	En 30 segundos está online con HTTPS
15.	Para dominio propio: Settings → Domains → agregar datiumtech.com.ar
5. Configuración del Dominio
Si registrás datiumtech.com.ar en NIC.ar o en un registrar privado:

Tipo de registro	Valor
A Record	IP de tu servidor hosting
CNAME www	datiumtech.com.ar
MX (email)	Configurar con Google Workspace o Zoho para info@datiumtech.com.ar

Propagación DNS: entre 15 minutos y 48 horas dependiendo del registrar.
6. Email Profesional info@datiumtech.com.ar
Opción A — Zoho Mail (gratis hasta 5 usuarios):
16.	Ir a zoho.com/es-xl/mail → Free Plan
17.	Agregar dominio datiumtech.com.ar
18.	Configurar los registros MX que te dan en tu panel de DNS
19.	Crear la casilla info@datiumtech.com.ar

Opción B — Google Workspace (USD 6/mes, mejor integración):
20.	workspace.google.com → Empezar prueba gratis
21.	Configurar dominio + crear cuenta Gmail corporativa
7. WhatsApp Business API
El botón flotante del sitio va al número +54 9 11 7652-2232. Cambios a hacer:
•	Registrar ese número como WhatsApp Business (app gratis en el celular)
•	Crear perfil: foto del logo DatiumTech, descripción del negocio, horarios
•	Activar respuestas rápidas para las consultas más comunes
•	Para escalar: contratar API oficial de Meta Business (necesitás BSPS como Leadsales o Treble)
8. SEO Inicial (primeros 30 días)
El sitio ya tiene meta description configurada. Tareas adicionales:
•	Crear Google Search Console → verificar propiedad con metatag
•	Crear Google Analytics 4 → insertar código de medición
•	Dar de alta en Google My Business (aunque sea servicio digital)
•	Registrar en Bing Webmaster Tools
•	Crear sitemap.xml (usar xml-sitemaps.com → subir al servidor → declarar en GSC)
9. Checklist de Lanzamiento
Marcá cada ítem antes de correr los primeros anuncios:

•	☐ index.html subido al servidor
•	☐ privacidad.html subido al servidor
•	☐ Web3Forms configurado con access_key real
•	☐ Test del formulario realizado (enviaste un mensaje de prueba)
•	☐ Recibiste el email de confirmación en info@datiumtech.com.ar
•	☐ Pixel de Meta instalado
•	☐ Evento Lead verificado en Events Manager
•	☐ HTTPS activo en el dominio
•	☐ Instagram de DatiumTech creado y con bio completa
•	☐ Cuenta de Meta Business Manager creada
•	☐ Tarjeta de crédito cargada en Meta Ads
•	☐ Primer anuncio configurado (ver Plan de Meta Ads)


DatiumTech — datiumtech@gmail.com — +54 9 11 7652-2232 

