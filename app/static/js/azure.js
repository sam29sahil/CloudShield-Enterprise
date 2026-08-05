/*
==========================================
CloudShield Enterprise
Azure Dashboard
==========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    initCounters();

    animateProgress();

    animateCards();

    dashboardGreeting();

    refreshTime();

});

/*==========================================
Counter Animation
==========================================*/

function initCounters() {

    const counters = document.querySelectorAll(
        ".service-content h2,.summary-card h2,.score-circle h2"
    );

    counters.forEach(counter => {

        const text = counter.innerText;

        const number = parseInt(text);

        if (isNaN(number)) return;

        let current = 0;

        const speed = Math.max(1, Math.ceil(number / 60));

        const timer = setInterval(() => {

            current += speed;

            if (current >= number) {

                current = number;

                clearInterval(timer);

            }

            if (text.includes("%")) {

                counter.innerText = current + "%";

            } else {

                counter.innerText = current;

            }

        }, 20);

    });

}

/*==========================================
Progress Bars
==========================================*/

function animateProgress() {

    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach(bar => {

        const width = bar.style.width;

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });

}

/*==========================================
Cards
==========================================*/

function animateCards() {

    document.querySelectorAll(".service-card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-8px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "";

        });

    });

}

/*==========================================
Greeting
==========================================*/

function dashboardGreeting() {

    const hour = new Date().getHours();

    let greeting = "Welcome";

    if(hour < 12){

        greeting = "Good Morning";

    }

    else if(hour < 18){

        greeting = "Good Afternoon";

    }

    else{

        greeting = "Good Evening";

    }

    console.log(greeting + " Azure Administrator");

}

/*==========================================
Clock
==========================================*/

function refreshTime(){

    const time = document.getElementById("dashboardTime");

    if(!time) return;

    setInterval(()=>{

        time.innerHTML =
            new Date().toLocaleTimeString();

    },1000);

}

/*==========================================
Toast
==========================================*/

function showToast(message){

    console.log(message);

}

/*==========================================
Auto Refresh Placeholder
==========================================*/

setInterval(()=>{

    console.log("Azure Dashboard Refresh");

},60000);