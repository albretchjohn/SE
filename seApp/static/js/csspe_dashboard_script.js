document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.querySelector(".search-form");
    const searchInput = document.querySelector(".search-form input[name='search_query']");
    
    searchForm.addEventListener("submit", function (event) {
        if (!searchInput.value.trim()) {
            event.preventDefault();
            alert("Please enter a search query.");
        }
    });
});
