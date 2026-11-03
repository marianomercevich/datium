(function () {
  var STORE = "dt_attr";
  var KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "gclid", "fbclid"];
  var attr = {};

  try {
    attr = JSON.parse(sessionStorage.getItem(STORE) || "{}");
  } catch (e) {
    attr = {};
  }

  var params = new URLSearchParams(location.search);
  KEYS.forEach(function (k) {
    var v = params.get(k);
    if (!v) return;
    attr[k] = v;
    if (!attr["first_" + k]) attr["first_" + k] = v;
  });

  if (!attr.landing) attr.landing = location.pathname || "/";
  if (!attr.referrer) {
    var ref = document.referrer || "";
    if (ref && ref.indexOf(location.hostname) === -1) attr.referrer = ref;
  }
  attr.last_page = location.pathname + location.search;
  try {
    sessionStorage.setItem(STORE, JSON.stringify(attr));
  } catch (e) { /* private mode */ }

  function canal() {
    var src = (attr.utm_source || "").toLowerCase();
    var med = (attr.utm_medium || "").toLowerCase();
    if (attr.gclid || src === "google" && med !== "organic") return "google_ads";
    if (src === "google" && (med === "organic" || med === "seo")) return "google_organico";
    if (attr.fbclid || /facebook|instagram|meta|ig/.test(src)) return "meta_ads";
    if (src === "whatsapp" || src === "wa") return "whatsapp";
    if (src === "linkedin") return "linkedin";
    if (src) return src + (med ? "_" + med : "");
    var r = attr.referrer || "";
    if (/google\./i.test(r)) return "google_organico";
    if (/bing\.|yahoo\./i.test(r)) return "buscador";
    if (/instagram|facebook|fb\.|l\.instagram/i.test(r)) return "redes";
    if (r) return "referral";
    return "directo";
  }

  function fire(name, payload) {
    payload = payload || {};
    payload.page_path = location.pathname;
    payload.canal = canal();
    if (typeof window.gtag === "function") window.gtag("event", name, payload);
    if (typeof window.fbq === "function") {
      if (name === "generate_lead") window.fbq("track", "Lead", payload);
      else window.fbq("trackCustom", name, payload);
    }
  }

  function hid(form, name, val) {
    var el = form.querySelector('[name="' + name + '"]');
    if (!el) {
      el = document.createElement("input");
      el.type = "hidden";
      el.name = name;
      form.appendChild(el);
    }
    el.value = val == null ? "" : String(val);
  }

  function fillForm(form) {
    var c = canal();
    hid(form, "canal", c);
    hid(form, "pagina", location.href);
    hid(form, "landing", attr.landing || "/");
    hid(form, "referrer", attr.referrer || "(directo)");
    KEYS.forEach(function (k) {
      hid(form, k, attr[k] || "");
    });
    hid(form, "first_utm_source", attr.first_utm_source || attr.utm_source || "");
    hid(form, "first_utm_campaign", attr.first_utm_campaign || attr.utm_campaign || "");
    var sub = form.querySelector('[name="subject"]');
    if (sub) {
      var base = sub.getAttribute("data-base") || sub.value.replace(/\s·\s[^\s]+$/, "");
      sub.setAttribute("data-base", base);
      sub.value = base + " · " + c;
    }
  }

  function msgBox(form, ok, text) {
    var box = form.querySelector(".form-msg, #form-msg");
    if (!box) {
      box = document.createElement("div");
      box.className = "form-msg";
      form.appendChild(box);
    }
    box.id = box.id || "form-msg";
    box.classList.remove("ok", "err");
    box.classList.add(ok ? "ok" : "err");
    box.style.display = "block";
    box.textContent = text;
  }

  function bindForms() {
    document.querySelectorAll("form.contact-form").forEach(function (form) {
      fillForm(form);
      if (form.dataset.dtBound) return;
      form.dataset.dtBound = "1";
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        fillForm(form);
        var btn = form.querySelector('[type="submit"]');
        var hp = form.querySelector('[name="botcheck"]');
        if (hp && (hp.checked || hp.value)) return;
        if (btn) {
          btn.disabled = true;
          btn.dataset.label = btn.textContent;
          btn.textContent = "Enviando…";
        }
        var data = new FormData(form);
        fetch("https://api.web3forms.com/submit", {
          method: "POST",
          body: data,
          headers: { Accept: "application/json" }
        })
          .then(function (r) { return r.json(); })
          .then(function (json) {
            if (json && json.success) {
              fire("generate_lead", {
                method: "form",
                servicio: data.get("servicio") || "",
                pago: data.get("pago") || ""
              });
              msgBox(form, true, "Recibido. Te contactamos a la brevedad.");
              form.reset();
              fillForm(form);
            } else {
              msgBox(form, false, "No se pudo enviar. Escribinos por WhatsApp.");
            }
          })
          .catch(function () {
            msgBox(form, false, "No se pudo enviar. Escribinos por WhatsApp.");
          })
          .finally(function () {
            if (btn) {
              btn.disabled = false;
              btn.textContent = btn.dataset.label || "QUIERO QUE ME CONTACTEN →";
            }
          });
      });
    });
  }

  function applyQueryToForm() {
    var servicio = params.get("servicio");
    var pago = params.get("pago");
    if (servicio) {
      document.querySelectorAll("select[name='servicio']").forEach(function (sel) {
        for (var i = 0; i < sel.options.length; i++) {
          if (sel.options[i].text.toLowerCase().indexOf(servicio.toLowerCase()) !== -1) {
            sel.selectedIndex = i;
            break;
          }
        }
      });
    }
    if (pago) {
      document.querySelectorAll("select[name='pago']").forEach(function (sel) {
        for (var i = 0; i < sel.options.length; i++) {
          if (sel.options[i].text.toLowerCase().indexOf(pago.toLowerCase()) !== -1) {
            sel.selectedIndex = i;
            break;
          }
        }
      });
    }
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a");
    if (!a || !a.href) return;

    if (/wa\.me|whatsapp\.com/i.test(a.href)) {
      fire("whatsapp_click", { link_url: a.href.split("?")[0] });
      try {
        var u = new URL(a.href);
        var t = u.searchParams.get("text") || "Hola DatiumTech";
        if (t.indexOf("[origen:") === -1) {
          u.searchParams.set("text", t + " [origen: " + canal() + "]");
          a.href = u.toString();
        }
      } catch (err) { /* ignore */ }
      return;
    }

    if (a.classList.contains("plan-cta") || a.classList.contains("nav-cta") || a.classList.contains("btn-main")) {
      fire("cta_click", { link_text: (a.textContent || "").trim().slice(0, 40) });
      if (a.dataset.pago || a.dataset.servicio) {
        var selPago = document.querySelector("select[name='pago']");
        var selSvc = document.querySelector("select[name='servicio']");
        if (selPago && a.dataset.pago) {
          for (var i = 0; i < selPago.options.length; i++) {
            if (selPago.options[i].text.indexOf(a.dataset.pago) !== -1) {
              selPago.selectedIndex = i;
              break;
            }
          }
        }
        if (selSvc && a.dataset.servicio) {
          for (var j = 0; j < selSvc.options.length; j++) {
            if (selSvc.options[j].text.indexOf(a.dataset.servicio) !== -1) {
              selSvc.selectedIndex = j;
              break;
            }
          }
        }
      }
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      bindForms();
      applyQueryToForm();
    });
  } else {
    bindForms();
    applyQueryToForm();
  }
})();
