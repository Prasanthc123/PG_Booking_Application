document.addEventListener("DOMContentLoaded", function () {
    // Your dynamic behavior or interaction can go here
    const dynamicElement = document.getElementById("dynamic-element");

    // Example: Add a click event listener to toggle animation
    dynamicElement.addEventListener("click", function () {
        dynamicElement.classList.toggle("animated");
    });
});