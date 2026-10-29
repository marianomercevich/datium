(function () {
  var KEY = "dt_consent";
  var bar = document.getElementById("cookie-bar");

  function hideBar() {
    if (bar) bar.setAttribute("hidden", "");
  }

  function loadAnalytics() {
    if (window.__dtAnalytics) return;
    window.__dtAnalytics = true;
    var ga = document.createElement("script");
    ga.async = true;
    ga.src = "https://www.googletagmanager.com/gtag/js?id=G-ZTE21X9Q9V";
    document.head.appendChild(ga);
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag("js", new Date());
    gtag("config", "G-ZTE21X9Q9V", { send_page_view: true, transport_type: "beacon" });

    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v;
      s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    fbq("init", "1927140795342157");
    fbq("track", "PageView");
  }

  var saved = localStorage.getItem(KEY);
  if (saved === "all") {
    loadAnalytics();
    hideBar();
  } else if (saved === "essentials") {
    hideBar();
  }

  document.getElementById("cookie-ok")?.addEventListener("click", function () {
    localStorage.setItem(KEY, "all");
    loadAnalytics();
    hideBar();
  });
  document.getElementById("cookie-no")?.addEventListener("click", function () {
    localStorage.setItem(KEY, "essentials");
    hideBar();
  });
})();
