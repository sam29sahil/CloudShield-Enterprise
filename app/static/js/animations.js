/*
=========================================================
 CloudShield Enterprise
 animations.js
 Enterprise Animation Engine
=========================================================
*/

(function () {
    "use strict";

    const CS = window.CloudShield || {};

    class AnimationEngine {

        constructor() {

            this.duration = 600;
            this.offset = 80;
            this.threshold = 0.15;

            this.observer = null;

            this.init();
        }

        init() {

            this.createObserver();

            this.registerFadeAnimations();

            this.registerSlideAnimations();

            this.registerScaleAnimations();

            this.registerRotateAnimations();

            this.registerHoverEffects();

            this.registerRippleEffects();

            this.registerNavbarAnimation();

            this.registerSidebarAnimation();

            this.registerCards();

            this.registerButtons();

            this.registerCounters();

        }

        createObserver() {

            this.observer = new IntersectionObserver(

                this.handleIntersect.bind(this),

                {
                    threshold: this.threshold,
                    rootMargin: "0px 0px -50px 0px"
                }

            );

            document.querySelectorAll("[data-animate]").forEach(element => {

                this.observer.observe(element);

            });

        }

        handleIntersect(entries) {

            entries.forEach(entry => {

                if (!entry.isIntersecting)
                    return;

                const element = entry.target;

                const animation =
                    element.dataset.animate || "fade-up";

                const delay =
                    Number(element.dataset.delay || 0);

                setTimeout(() => {

                    element.classList.add("animated");

                    element.classList.add(animation);

                }, delay);

                this.observer.unobserve(element);

            });

        }

        animate(element, animation) {

            element.classList.remove(animation);

            void element.offsetWidth;

            element.classList.add(animation);

        }

        fadeIn(element) {

            this.animate(element, "fade-in");

        }

        fadeOut(element) {

            this.animate(element, "fade-out");

        }

        slideUp(element) {

            this.animate(element, "slide-up");

        }

        slideDown(element) {

            this.animate(element, "slide-down");

        }

        slideLeft(element) {

            this.animate(element, "slide-left");

        }

        slideRight(element) {

            this.animate(element, "slide-right");

        }

        zoomIn(element) {

            this.animate(element, "zoom-in");

        }

        zoomOut(element) {

            this.animate(element, "zoom-out");

        }

        bounce(element) {

            this.animate(element, "bounce");

        }

        pulse(element) {

            this.animate(element, "pulse");

        }

        shake(element) {

            this.animate(element, "shake");

        }

        rotate(element) {

            this.animate(element, "rotate");

        }

        flash(element) {

            this.animate(element, "flash");

        }

        registerFadeAnimations() {

            document.querySelectorAll(".fade-on-load")
                .forEach((element, index) => {

                    setTimeout(() => {

                        element.classList.add("fade-in");

                    }, index * 100);

                });

        }

        registerSlideAnimations() {

            document.querySelectorAll(".slide-on-load")
                .forEach((element, index) => {

                    setTimeout(() => {

                        element.classList.add("slide-up");

                    }, index * 120);

                });

        }

        registerScaleAnimations() {

            document.querySelectorAll(".scale-on-load")
                .forEach((element, index) => {

                    setTimeout(() => {

                        element.classList.add("zoom-in");

                    }, index * 120);

                });

        }

        registerRotateAnimations() {

            document.querySelectorAll(".rotate-hover")
                .forEach(element => {

                    element.addEventListener("mouseenter", () => {

                        element.classList.add("rotate");

                    });

                    element.addEventListener("mouseleave", () => {

                        element.classList.remove("rotate");

                    });

                });

        }

        registerHoverEffects() {

            document.querySelectorAll(".card")
                .forEach(card => {

                    card.addEventListener("mouseenter", () => {

                        card.classList.add("card-hover");

                    });

                    card.addEventListener("mouseleave", () => {

                        card.classList.remove("card-hover");

                    });

                });

        }

        registerRippleEffects() {

            document.querySelectorAll(".btn-ripple")
                .forEach(button => {

                    button.addEventListener("click", e => {

                        const ripple =
                            document.createElement("span");

                        ripple.className = "ripple";

                        const rect =
                            button.getBoundingClientRect();

                        ripple.style.left =
                            `${e.clientX - rect.left}px`;

                        ripple.style.top =
                            `${e.clientY - rect.top}px`;

                        button.appendChild(ripple);

                        setTimeout(() => {

                            ripple.remove();

                        }, 700);

                    });

                });

        }

        registerNavbarAnimation() {

            const navbar =
                document.querySelector(".top-navbar");

            if (!navbar)
                return;

            let previous = 0;

            window.addEventListener("scroll", () => {

                const current =
                    window.pageYOffset;

                if (current > previous && current > 80) {

                    navbar.classList.add("navbar-hide");

                } else {

                    navbar.classList.remove("navbar-hide");

                }

                previous = current;

            });

        }

        registerSidebarAnimation() {

            const sidebar =
                document.querySelector(".sidebar");

            if (!sidebar)
                return;

            sidebar.classList.add("sidebar-ready");

            requestAnimationFrame(() => {

                sidebar.classList.add("sidebar-visible");

            });

        }
        registerCards() {

            const cards = document.querySelectorAll(
                ".dashboard-card,.stat-card,.glass-card,.feature-card"
            );

            cards.forEach((card, index) => {

                card.style.opacity = "0";
                card.style.transform = "translateY(25px)";

                setTimeout(() => {

                    card.style.transition =
                        "all .55s cubic-bezier(.22,.61,.36,1)";

                    card.style.opacity = "1";
                    card.style.transform = "translateY(0)";

                }, 80 * index);

            });

        }

        registerButtons() {

            document.querySelectorAll(".btn").forEach(button => {

                button.addEventListener("mouseenter", () => {

                    button.style.transform =
                        "translateY(-3px) scale(1.02)";

                });

                button.addEventListener("mouseleave", () => {

                    button.style.transform = "";

                });

            });

        }

        registerCounters() {

            document.querySelectorAll("[data-counter]")
                .forEach(counter => {

                    const target =
                        parseInt(counter.dataset.counter);

                    const duration =
                        parseInt(counter.dataset.duration || 1800);

                    this.animateCounter(counter, target, duration);

                });

        }

        animateCounter(element, target, duration) {

            let start = 0;

            const increment =
                target / (duration / 16);

            const update = () => {

                start += increment;

                if (start >= target) {

                    element.textContent =
                        target.toLocaleString();

                    return;

                }

                element.textContent =
                    Math.floor(start).toLocaleString();

                requestAnimationFrame(update);

            };

            update();

        }

        animateProgressBars() {

            document.querySelectorAll(".progress-bar")
                .forEach(bar => {

                    const width =
                        bar.dataset.width || "0";

                    bar.style.width = "0";

                    requestAnimationFrame(() => {

                        bar.style.transition =
                            "width 1.4s ease";

                        bar.style.width =
                            width + "%";

                    });

                });

        }

        animateCircularProgress() {

            document.querySelectorAll(".circle-progress")
                .forEach(circle => {

                    const percent =
                        Number(circle.dataset.percent);

                    const radius =
                        Number(circle.dataset.radius || 52);

                    const circumference =
                        2 * Math.PI * radius;

                    const progress =
                        circumference -
                        percent / 100 * circumference;

                    circle.style.strokeDasharray =
                        circumference;

                    circle.style.strokeDashoffset =
                        circumference;

                    setTimeout(() => {

                        circle.style.transition =
                            "stroke-dashoffset 1.4s ease";

                        circle.style.strokeDashoffset =
                            progress;

                    }, 300);

                });

        }

        typingEffect(selector) {

            const element =
                document.querySelector(selector);

            if (!element)
                return;

            const text =
                element.dataset.text || element.textContent;

            element.textContent = "";

            let index = 0;

            const timer = setInterval(() => {

                element.textContent += text[index];

                index++;

                if (index >= text.length) {

                    clearInterval(timer);

                }

            }, 45);

        }

        floatingElements() {

            document.querySelectorAll(".floating")
                .forEach((item, index) => {

                    const duration =
                        2500 + index * 400;

                    let direction = 1;

                    setInterval(() => {

                        direction *= -1;

                        item.style.transform =
                            `translateY(${direction * 8}px)`;

                    }, duration);

                });

        }

        mouseParallax() {

            const hero =
                document.querySelector(".hero");

            if (!hero)
                return;

            hero.addEventListener("mousemove", e => {

                const x =
                    (e.clientX / window.innerWidth - .5) * 30;

                const y =
                    (e.clientY / window.innerHeight - .5) * 30;

                hero.querySelectorAll(".parallax")
                    .forEach(layer => {

                        layer.style.transform =
                            `translate(${x}px,${y}px)`;

                    });

            });

        }

        dashboardWidgets() {

            document.querySelectorAll(".widget")
                .forEach(widget => {

                    widget.addEventListener("mouseenter", () => {

                        widget.style.transform =
                            "translateY(-8px)";

                        widget.style.boxShadow =
                            "0 20px 45px rgba(0,0,0,.15)";

                    });

                    widget.addEventListener("mouseleave", () => {

                        widget.style.transform = "";

                        widget.style.boxShadow = "";

                    });

                });

        }

        loadingTransition() {

            const loader =
                document.querySelector(".loading-screen");

            if (!loader)
                return;

            window.addEventListener("load", () => {

                loader.classList.add("fade-out");

                setTimeout(() => {

                    loader.remove();

                }, 700);

            });

        }

        skeletonLoader() {

            document.querySelectorAll(".skeleton")
                .forEach(item => {

                    item.classList.add("loading");

                });

        }

        notificationAnimation() {

            document.querySelectorAll(".notification")
                .forEach(notification => {

                    notification.classList.add("slide-right");

                    setTimeout(() => {

                        notification.classList.remove("slide-right");

                    }, 600);

                });

        }

        modalAnimation() {

            document.querySelectorAll(".modal")
                .forEach(modal => {

                    modal.addEventListener("shown.bs.modal", () => {

                        const dialog =
                            modal.querySelector(".modal-dialog");

                        dialog.classList.add("zoom-in");

                    });

                });

        }

        scrollTopAnimation() {

            const button =
                document.querySelector(".scroll-top");

            if (!button)
                return;

            window.addEventListener("scroll", () => {

                if (window.scrollY > 500) {

                    button.classList.add("show");

                } else {

                    button.classList.remove("show");

                }

            });

        }

        pageTransition() {

            document.querySelectorAll("a")
                .forEach(link => {

                    if (
                        link.target === "_blank" ||
                        link.href.startsWith("#")
                    )
                        return;

                    link.addEventListener("click", () => {

                        document.body.classList.add(
                            "page-transition"
                        );

                    });

                });

        }
        staggerAnimation(selector, delay = 100) {

            const elements = document.querySelectorAll(selector);

            elements.forEach((element, index) => {

                element.style.opacity = "0";
                element.style.transform = "translateY(20px)";

                setTimeout(() => {

                    element.style.transition =
                        "all .55s cubic-bezier(.22,.61,.36,1)";

                    element.style.opacity = "1";
                    element.style.transform = "translateY(0)";

                }, index * delay);

            });

        }

        scrollReveal() {

            const observer = new IntersectionObserver(entries => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting)
                        return;

                    entry.target.classList.add("revealed");

                    observer.unobserve(entry.target);

                });

            }, {
                threshold: .2
            });

            document.querySelectorAll(".reveal")
                .forEach(item => observer.observe(item));

        }

        animateCharts() {

            document.querySelectorAll("canvas")
                .forEach(chart => {

                    chart.style.opacity = "0";

                    requestAnimationFrame(() => {

                        chart.style.transition =
                            "opacity .8s ease";

                        chart.style.opacity = "1";

                    });

                });

        }

        heroEffects() {

            const hero =
                document.querySelector(".hero");

            if (!hero)
                return;

            window.addEventListener("scroll", () => {

                const offset =
                    window.pageYOffset * .35;

                hero.style.backgroundPositionY =
                    `${offset}px`;

            });

        }

        scanPulse() {

            document.querySelectorAll(".scan-live")
                .forEach(scan => {

                    setInterval(() => {

                        scan.classList.add("pulse");

                        setTimeout(() => {

                            scan.classList.remove("pulse");

                        }, 1000);

                    }, 3000);

                });

        }

        findingsAnimation() {

            document.querySelectorAll(".finding-item")
                .forEach((item, index) => {

                    item.style.opacity = "0";

                    setTimeout(() => {

                        item.style.transition =
                            ".45s ease";

                        item.style.opacity = "1";

                    }, index * 80);

                });

        }

        tableAnimation() {

            document.querySelectorAll("tbody tr")
                .forEach((row, index) => {

                    row.style.opacity = "0";

                    row.style.transform =
                        "translateX(-12px)";

                    setTimeout(() => {

                        row.style.transition =
                            ".4s ease";

                        row.style.opacity = "1";

                        row.style.transform =
                            "translateX(0)";

                    }, index * 35);

                });

        }

        sidebarCollapse() {

            const toggle =
                document.querySelector(".sidebar-toggle");

            const sidebar =
                document.querySelector(".sidebar");

            if (!toggle || !sidebar)
                return;

            toggle.addEventListener("click", () => {

                sidebar.classList.toggle("collapsed");

            });

        }

        resizeHandler() {

            let timer;

            window.addEventListener("resize", () => {

                clearTimeout(timer);

                timer = setTimeout(() => {

                    document.body.classList.add(
                        "resized"
                    );

                    setTimeout(() => {

                        document.body.classList.remove(
                            "resized"
                        );

                    }, 250);

                }, 150);

            });

        }

        optimize() {

            if ("requestIdleCallback" in window) {

                requestIdleCallback(() => {

                    this.animateProgressBars();

                    this.animateCircularProgress();

                    this.typingEffect(".typing");

                    this.floatingElements();

                    this.mouseParallax();

                    this.dashboardWidgets();

                    this.loadingTransition();

                    this.skeletonLoader();

                    this.notificationAnimation();

                    this.modalAnimation();

                    this.scrollTopAnimation();

                    this.pageTransition();

                    this.scrollReveal();

                    this.animateCharts();

                    this.heroEffects();

                    this.scanPulse();

                    this.findingsAnimation();

                    this.tableAnimation();

                    this.sidebarCollapse();

                    this.resizeHandler();

                });

            } else {

                this.animateProgressBars();

                this.animateCircularProgress();

                this.typingEffect(".typing");

                this.floatingElements();

                this.mouseParallax();

                this.dashboardWidgets();

                this.loadingTransition();

                this.skeletonLoader();

                this.notificationAnimation();

                this.modalAnimation();

                this.scrollTopAnimation();

                this.pageTransition();

                this.scrollReveal();

                this.animateCharts();

                this.heroEffects();

                this.scanPulse();

                this.findingsAnimation();

                this.tableAnimation();

                this.sidebarCollapse();

                this.resizeHandler();

            }

        }

    }

    document.addEventListener("DOMContentLoaded", () => {

        const animations = new AnimationEngine();

        animations.optimize();

        window.CloudShield =
            window.CloudShield || {};

        window.CloudShield.Animations =
            animations;

    });

})();