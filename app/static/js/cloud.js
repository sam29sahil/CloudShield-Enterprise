/*
=========================================
CloudShield Enterprise
Cloud JavaScript
=========================================
*/

document.addEventListener("DOMContentLoaded",function(){

console.log("Cloud Module Loaded");

});

/* =====================================
Refresh
===================================== */

function refreshCloud(){

location.reload();

}

/* =====================================
Copy
===================================== */

function copyCloud(text){

navigator.clipboard.writeText(text);

showCloudToast("Copied Successfully");

}

/* =====================================
Toast
===================================== */

function showCloudToast(message){

console.log(message);

}

/* =====================================
Search
===================================== */

function cloudSearch(id,input){

let value=input.value.toLowerCase();

let rows=document.querySelectorAll("#"+id+" tbody tr");

rows.forEach(function(row){

if(row.innerText.toLowerCase().includes(value))

row.style.display="";

else

row.style.display="none";

});

}

/* =====================================
Auto Refresh
===================================== */

setInterval(function(){

console.log("Cloud Auto Refresh");

},300000);

/* =====================================
Animation
===================================== */

document.querySelectorAll(".cloud-card").forEach(function(card){

card.addEventListener("mouseenter",function(){

card.classList.add("shadow-lg");

});

card.addEventListener("mouseleave",function(){

card.classList.remove("shadow-lg");

});

});
/*
==================================================
CloudShield Enterprise
Cloud Dashboard
==================================================
*/

document.addEventListener("DOMContentLoaded", function () {

    initializeCloudDashboard();

});

/* ==========================================
   Initialize
========================================== */

function initializeCloudDashboard() {

    animateCounters();

    animateCards();

    animateSecurityCircle();

    floatingHero();

}

/* ==========================================
   Counter Animation
========================================== */

function animateCounters() {

    document.querySelectorAll(".counter").forEach(counter => {

        let target = parseInt(counter.innerText);

        if (isNaN(target)) return;

        let value = 0;

        let speed = Math.max(10, target / 50);

        counter.innerText = "0";

        let timer = setInterval(() => {

            value += speed;

            if (value >= target) {

                counter.innerText = target;

                clearInterval(timer);

            } else {

                counter.innerText = Math.floor(value);

            }

        }, 20);

    });

}

/* ==========================================
   Card Animation
========================================== */

function animateCards() {

    const cards = document.querySelectorAll(".stat-card,.provider-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(40px)";

        setTimeout(() => {

            card.style.transition = ".6s";

            card.style.opacity = "1";

            card.style.transform = "translateY(0px)";

        }, index * 120);

    });

}

/* ==========================================
   Security Score Circle
========================================== */

function animateSecurityCircle() {

    const circle = document.querySelector(".score-progress");

    const score = document.getElementById("securityScore");

    if (!circle || !score) return;

    const percentage = parseInt(score.innerText);

    const radius = 70;

    const circumference = 2 * Math.PI * radius;

    circle.style.strokeDasharray = circumference;

    const offset = circumference - (percentage / 100) * circumference;

    circle.style.strokeDashoffset = circumference;

    setTimeout(() => {

        circle.style.transition = "2s ease";

        circle.style.strokeDashoffset = offset;

    }, 500);

}

/* ==========================================
   Floating Hero Effect
========================================== */

function floatingHero() {

    const hero = document.querySelector(".cloud-hero");

    if (!hero) return;

    hero.addEventListener("mousemove", function (e) {

        const x = (e.clientX - hero.offsetWidth / 2) / 60;

        const y = (e.clientY - hero.offsetHeight / 2) / 60;

        hero.style.transform =
            `rotateY(${x}deg) rotateX(${-y}deg)`;

    });

    hero.addEventListener("mouseleave", function () {

        hero.style.transform =
            "rotateX(0deg) rotateY(0deg)";

    });

}

/* ==========================================
   Refresh Dashboard
========================================== */

function refreshCloudDashboard() {

    location.reload();

}

/* ==========================================
   Toast
========================================== */

function showCloudToast(message) {

    console.log(message);

}

/* ==========================================
   Auto Refresh Every 5 Minutes
========================================== */

setInterval(function () {

    console.log("Refreshing dashboard...");

}, 300000);