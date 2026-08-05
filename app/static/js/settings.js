/*
=========================================
CloudShield Enterprise
Settings JavaScript
=========================================
*/

document.addEventListener("DOMContentLoaded", function () {

    initializeTabs();

    initializePasswordStrength();

    initializeUnsavedChanges();

    initializeAnimations();

    initializeSaveButtons();

});


/* =====================================
Remember Active Tab
===================================== */

function initializeTabs() {

    const tabs = document.querySelectorAll(
        '#settingsTabs .nav-link'
    );

    const savedTab = localStorage.getItem(
        "settings-active-tab"
    );

    if (savedTab) {

        const tab = document.querySelector(
            '#settingsTabs a[href="' + savedTab + '"]'
        );

        if (tab) {

            new bootstrap.Tab(tab).show();

        }

    }

    tabs.forEach(tab => {

        tab.addEventListener("shown.bs.tab", function () {

            localStorage.setItem(

                "settings-active-tab",

                this.getAttribute("href")

            );

        });

    });

}


/* =====================================
Password Strength
===================================== */

function initializePasswordStrength() {

    const password = document.querySelector(

        'input[name$="new_password"]'

    );

    if (!password) return;

    password.addEventListener("input", function () {

        const value = this.value;

        let score = 0;

        if (value.length >= 8)
            score++;

        if (/[A-Z]/.test(value))
            score++;

        if (/[a-z]/.test(value))
            score++;

        if (/[0-9]/.test(value))
            score++;

        if (/[^A-Za-z0-9]/.test(value))
            score++;

        let text = "";

        switch (score) {

            case 0:
            case 1:
                text = "Very Weak";
                break;

            case 2:
                text = "Weak";
                break;

            case 3:
                text = "Medium";
                break;

            case 4:
                text = "Strong";
                break;

            default:
                text = "Very Strong";

        }

        this.setCustomValidity("");

        this.title = "Password Strength : " + text;

    });

}


/* =====================================
Unsaved Changes
===================================== */

function initializeUnsavedChanges() {

    let changed = false;

    document.querySelectorAll(

        "input, select, textarea"

    ).forEach(field => {

        field.addEventListener("change", () => {

            changed = true;

        });

    });

    window.addEventListener(

        "beforeunload",

        function (e) {

            if (!changed)

                return;

            e.preventDefault();

            e.returnValue = "";

        }

    );

    document.querySelectorAll("form").forEach(form => {

        form.addEventListener("submit", () => {

            changed = false;

        });

    });

}


/* =====================================
Animations
===================================== */

function initializeAnimations() {

    document.querySelectorAll(".card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-4px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "";

        });

    });

}


/* =====================================
Save Button Animation
===================================== */

function initializeSaveButtons() {

    document.querySelectorAll(

        'button[type="submit"], input[type="submit"]'

    ).forEach(button => {

        button.addEventListener("click", function () {

            const original = this.value || this.innerHTML;

            if (this.tagName === "INPUT") {

                this.value = "Saving...";

            }

            else {

                this.innerHTML =

                    '<span class="spinner-border spinner-border-sm me-2"></span>Saving...';

            }

            this.disabled = true;

            setTimeout(() => {

                if (this.tagName === "INPUT") {

                    this.value = original;

                }

                else {

                    this.innerHTML = original;

                }

                this.disabled = false;

            }, 1200);

        });

    });

}