/* Joosep Fingling - portfolio
   Language toggle (persisted), tag filter on the home page, image lightbox. */
(function () {
  var KEY = "site-lang";

  function apply(lang) {
    if (lang !== "en") lang = "et";   // anything unexpected falls back to the default
    var root = document.documentElement;
    root.dataset.lang = lang;
    root.setAttribute("lang", lang);
    try { localStorage.setItem(KEY, lang); } catch (e) {}
  }

  // Initial language (also set inline in <head> to avoid a flash).
  var start = "et";
  try { start = localStorage.getItem(KEY) || "et"; } catch (e) {}
  apply(start);

  // ---- tag filter (home page only: it has the cards and the filter bar) ----
  function tagFromUrl() {
    var m = /[?&]tag=([^&#]*)/.exec(location.search);
    return m ? decodeURIComponent(m[1]).toLowerCase().replace(/[^a-z0-9-]/g, "") : "";
  }

  function filter(key) {
    var bar = document.getElementById("filters");
    var cards = document.querySelectorAll(".card[data-tags]");
    var shown = 0;
    cards.forEach(function (card) {
      var on = !key || (" " + card.getAttribute("data-tags") + " ").indexOf(" " + key + " ") >= 0;
      card.hidden = !on;
      if (on) shown++;
    });
    document.querySelectorAll(".projsec").forEach(function (sec) {
      sec.hidden = !sec.querySelector(".card[data-tags]:not([hidden])");
    });
    document.querySelectorAll(".tag[data-tag]").forEach(function (tag) {
      tag.classList.toggle("active", !!key && tag.getAttribute("data-tag") === key);
    });

    var sample = key && document.querySelector('.tag[data-tag="' + key + '"]');
    if (!sample) {                       // no filter, or a tag no project has
      bar.hidden = true;
      if (key) { cards.forEach(function (c) { c.hidden = false; });
                 document.querySelectorAll(".projsec").forEach(function (s) { s.hidden = false; }); }
      return;
    }
    var label = bar.querySelector(".filter-tag");
    label.className = sample.className.replace(/\bactive\b/, "") + " filter-tag";
    label.innerHTML = sample.innerHTML;
    bar.querySelector(".filter-count").innerHTML =
      '<span class="lang-et">' + shown + (shown === 1 ? " projekt" : " projekti") + "</span>" +
      '<span class="lang-en">' + shown + (shown === 1 ? " project" : " projects") + "</span>";
    bar.hidden = false;
  }

  function setTag(key, push) {
    var url = location.pathname + (key ? "?tag=" + key : "");
    if (push) history.pushState({ tag: key }, "", url);
    filter(key);
  }

  document.addEventListener("DOMContentLoaded", function () {
    // Language toggle buttons
    document.querySelectorAll(".langtoggle button[data-set]").forEach(function (btn) {
      btn.addEventListener("click", function () { apply(btn.getAttribute("data-set")); });
    });

    var bar = document.getElementById("filters");
    if (bar) {
      filter(tagFromUrl());
      if (tagFromUrl()) bar.scrollIntoView();
      document.addEventListener("click", function (e) {
        var tag = e.target.closest("a.tag[data-tag]");
        if (!tag || e.ctrlKey || e.metaKey || e.shiftKey || e.button) return;
        e.preventDefault();
        var key = tag.getAttribute("data-tag");
        var next = key === tagFromUrl() ? "" : key;      // clicking the active tag clears it
        setTag(next, true);
        if (next) bar.scrollIntoView();
      });
      bar.querySelector(".filter-clear").addEventListener("click", function () { setTag("", true); });
      window.addEventListener("popstate", function () { filter(tagFromUrl()); });
    }

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
