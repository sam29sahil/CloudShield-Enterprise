document.addEventListener("DOMContentLoaded", function () {

    console.log("CloudShield Enterprise Loaded");

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {
            card.style.transition = "0.3s";
        });

    });

});