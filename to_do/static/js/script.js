document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("theme-toggle");
    const body = document.body;

    toggleBtn.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        if (body.classList.contains("dark-mode")) {
            toggleBtn.classList.remove("btn-dark");
            toggleBtn.classList.add("btn-light");
            toggleBtn.innerHTML = "☀️ Light Mode";
        } else {
            toggleBtn.classList.remove("btn-light");
            toggleBtn.classList.add("btn-dark");
            toggleBtn.innerHTML = "🌙 Dark Mode";
        }
    });
});
