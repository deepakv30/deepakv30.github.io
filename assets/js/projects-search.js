(function () {
  "use strict";

  const searchInput = document.getElementById("projects-search");
  const clearBtn = document.getElementById("projects-search-clear");
  const emptyEl = document.getElementById("projects-empty");
  const countEl = document.getElementById("projects-count");
  const cards = document.querySelectorAll("[data-project-card]");

  if (!searchInput || !cards.length) {
    return;
  }

  const total = cards.length;

  function normalize(value) {
    return (value || "").toLowerCase().trim();
  }

  function applyFilter() {
    const query = normalize(searchInput.value);
    let visible = 0;

    cards.forEach((card) => {
      const haystack = normalize(card.getAttribute("data-search"));
      const match = !query || haystack.indexOf(query) !== -1;
      card.hidden = !match;
      if (match) {
        visible += 1;
      }
    });

    if (emptyEl) {
      emptyEl.hidden = visible !== 0;
    }

    if (countEl) {
      if (query) {
        countEl.textContent = visible === 1
          ? "1 project matches your search."
          : visible + " projects match your search.";
      } else {
        countEl.textContent = total + " projects.";
      }
    }
  }

  searchInput.addEventListener("input", applyFilter);

  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      searchInput.value = "";
      applyFilter();
      searchInput.focus();
    });
  }

  const params = new URLSearchParams(window.location.search);
  if (params.has("q")) {
    searchInput.value = params.get("q") || "";
  }

  applyFilter();
})();
