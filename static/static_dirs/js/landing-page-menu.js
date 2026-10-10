var menuToggle = document.getElementById("menuToggle");

function setMenu(open) {
    menuToggle.setAttribute("aria-expanded", open);
    menuToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.classList.toggle("menu-open", open);
}

menuToggle.addEventListener("click", function () {
    setMenu(menuToggle.getAttribute("aria-expanded") !== "true");
});
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setMenu(false);
});
// Close the sheet if the screen grows past the mobile breakpoint (e.g. tablet rotation)
window.matchMedia("(min-width: 761px)").addEventListener("change", function () {
    setMenu(false);
});
