/* Joosep Fingling — portfolio
   Language toggle (persisted) + image lightbox. */
(function () {
  var KEY = "site-lang";

  function apply(lang) {
    var root = document.documentElement;
    root.dataset.lang = lang;
    root.setAttribute("lang", lang);
    try { localStorage.setItem(KEY, lang); } catch (e) {}
  }

  // Initial language (also set inline in <head> to avoid a flash).
  var start = "et";
  try { start = localStorage.getItem(KEY) || "et"; } catch (e) {}
  apply(start);

  document.addEventListener("DOMContentLoaded", function () {
    // Language toggle buttons
    document.querySelectorAll(".langtoggle button[data-set]").forEach(function (btn) {
      btn.addEventListener("click", function () { apply(btn.getAttribute("data-set")); });
    });

    // Lightbox for image galleries
    var lb = document.getElementById("lightbox");
    if (lb) {
      var lbImg = lb.querySelector("img");
      document.querySelectorAll(".gallery").forEach(function (g) {
        g.addEventListener("click", function (e) {
          var img = e.target.closest("img");
          if (!img) return;
          lbImg.src = img.currentSrc || img.src;
          lbImg.alt = img.alt || "";
          lb.classList.add("open");
        });
      });
      lb.addEventListener("click", function () { lb.classList.remove("open"); });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") lb.classList.remove("open");
      });
    }
  });
})();
