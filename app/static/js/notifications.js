/*
=========================================
CloudShield Enterprise
Notification Center
=========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    initializeNotifications();

});


function initializeNotifications() {

    animateNotifications();

    bindDeleteButtons();

    bindReadButtons();

    initializeSearch();

}


// ====================================
// Animation
// ====================================

function animateNotifications() {

    const items = document.querySelectorAll(".notification-item");

    items.forEach((item, index) => {

        item.style.opacity = "0";

        item.style.transform = "translateY(15px)";

        setTimeout(() => {

            item.style.transition = ".35s";

            item.style.opacity = "1";

            item.style.transform = "translateY(0)";

        }, index * 70);

    });

}


// ====================================
// Delete Confirmation
// ====================================

function bindDeleteButtons() {

    document.querySelectorAll(".btn-outline-danger").forEach(btn => {

        btn.addEventListener("click", function(e){

            if(!confirm("Delete this notification?")){

                e.preventDefault();

            }

        });

    });

}


// ====================================
// Mark Read
// ====================================

function bindReadButtons() {

    document.querySelectorAll(".btn-success").forEach(btn => {

        btn.addEventListener("click", function(){

            const card = this.closest(".notification-item");

            if(card){

                card.classList.remove("notification-unread");

            }

        });

    });

}


// ====================================
// Search
// ====================================

function initializeSearch(){

    const search = document.getElementById("notificationSearch");

    if(!search) return;

    search.addEventListener("keyup", function(){

        const value = this.value.toLowerCase();

        document.querySelectorAll(".notification-item").forEach(item=>{

            item.style.display = item.innerText.toLowerCase().includes(value)

                ? ""

                : "none";

        });

    });

}


// ====================================
// Auto Refresh Badge
// ====================================

function updateBadge(){

    const badge = document.getElementById("notificationBadge");

    if(!badge) return;

    const unread = document.querySelectorAll(".notification-unread").length;

    badge.innerText = unread;

    if(unread===0){

        badge.style.display="none";

    }

}


// ====================================
// Refresh Every Minute
// ====================================

setInterval(updateBadge,60000);