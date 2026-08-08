/*
=========================================================
 CloudShield Enterprise
 dashboard.js
 Enterprise Dashboard Controller
=========================================================
*/

(function () {

    "use strict";

    const CS = window.CloudShield || {};

    class Dashboard {

        constructor() {

            this.refreshInterval = 30000;

            this.stats = {};

            this.charts = {};

            this.notifications = [];

            this.init();

        }

        init() {

            this.cacheDOM();

            this.bindEvents();

            this.initializeCards();

            this.initializeCounters();

            this.initializeWidgets();

            this.initializeQuickActions();

            this.initializeActivity();

            this.initializeHealth();

            this.initializeSearch();

            this.initializeNotifications();

            this.startAutoRefresh();

        }

        cacheDOM() {

            this.dashboard =
                document.querySelector(".dashboard");

            this.hero =
                document.querySelector(".dashboard-hero");

            this.statsCards =
                document.querySelectorAll(".stat-card");

            this.activity =
                document.querySelector(".activity-list");

            this.health =
                document.querySelector(".system-health");

            this.search =
                document.querySelector("#dashboard-search");

            this.notificationBadge =
                document.querySelector(".notification-count");

        }

        bindEvents() {

            window.addEventListener(

                "resize",

                this.handleResize.bind(this)

            );

            document.addEventListener(

                "visibilitychange",

                this.handleVisibility.bind(this)

            );

        }

        initializeCards() {

            this.statsCards.forEach((card, index) => {

                card.style.opacity = "0";

                card.style.transform =
                    "translateY(20px)";

                setTimeout(() => {

                    card.style.transition =
                        ".5s ease";

                    card.style.opacity = "1";

                    card.style.transform =
                        "translateY(0)";

                }, index * 120);

            });

        }

        initializeCounters() {

            document.querySelectorAll(

                "[data-stat]"

            ).forEach(counter => {

                const target =
                    Number(counter.dataset.stat);

                this.animateCounter(

                    counter,

                    target

                );

            });

        }

        animateCounter(

            element,

            target,

            duration = 1800

        ) {

            let current = 0;

            const increment =
                target / (duration / 16);

            const update = () => {

                current += increment;

                if (current >= target) {

                    element.textContent =
                        target.toLocaleString();

                    return;

                }

                element.textContent =
                    Math.floor(current)
                    .toLocaleString();

                requestAnimationFrame(update);

            };

            update();

        }

        initializeWidgets() {

            document.querySelectorAll(

                ".dashboard-widget"

            ).forEach(widget => {

                widget.addEventListener(

                    "mouseenter",

                    () => {

                        widget.classList.add(

                            "widget-hover"

                        );

                    }

                );

                widget.addEventListener(

                    "mouseleave",

                    () => {

                        widget.classList.remove(

                            "widget-hover"

                        );

                    }

                );

            });

        }

        initializeQuickActions() {

            document.querySelectorAll(

                ".quick-action"

            ).forEach(button => {

                button.addEventListener(

                    "click",

                    e => {

                        const action =
                            e.currentTarget.dataset.action;

                        this.executeAction(action);

                    }

                );

            });

        }

        executeAction(action) {

            switch (action) {

                case "scan":

                    window.location =
                        "/scanner";

                    break;

                case "assets":

                    window.location =
                        "/assets";

                    break;

                case "reports":

                    window.location =
                        "/reports";

                    break;

                case "settings":

                    window.location =
                        "/settings";

                    break;

                default:

                    console.warn(

                        "Unknown action:",

                        action

                    );

            }

        }

        initializeActivity() {

            const items =
                document.querySelectorAll(

                    ".activity-item"

                );

            items.forEach((item, index) => {

                item.style.opacity = "0";

                setTimeout(() => {

                    item.style.transition =
                        ".45s ease";

                    item.style.opacity = "1";

                }, index * 100);

            });

        }

        initializeHealth() {

            document.querySelectorAll(

                ".health-progress"

            ).forEach(progress => {

                const value =
                    progress.dataset.value;

                progress.style.width = "0";

                requestAnimationFrame(() => {

                    progress.style.transition =
                        "width 1.3s ease";

                    progress.style.width =
                        value + "%";

                });

            });

        }
        startAutoRefresh() {

            this.refreshTimer = setInterval(() => {

                this.refreshDashboard();

            }, this.refreshInterval);

        }

        async refreshDashboard() {

            try {

                await Promise.all([

                    this.loadStatistics(),
                    this.loadNotifications(),
                    this.loadRecentActivity(),
                    this.loadSystemHealth()

                ]);

            } catch (error) {

                console.error(
                    "Dashboard refresh failed:",
                    error
                );

            }

        }

        async loadStatistics() {

            try {

                const response = await fetch(
                    "/api/dashboard/stats"
                );

                if (!response.ok)
                    return;

                const data =
                    await response.json();

                this.updateStatistics(data);

            } catch (error) {

                console.error(error);

            }

        }

        updateStatistics(data) {

            Object.keys(data).forEach(key => {

                const element =
                    document.querySelector(
                        `[data-stat-name="${key}"]`
                    );

                if (!element)
                    return;

                this.animateCounter(
                    element,
                    Number(data[key])
                );

            });

        }

        async loadNotifications() {

            try {

                const response =
                    await fetch(
                        "/api/notifications"
                    );

                if (!response.ok)
                    return;

                const notifications =
                    await response.json();

                this.notifications =
                    notifications;

                this.renderNotifications();

            } catch (error) {

                console.error(error);

            }

        }

        renderNotifications() {

            const list =
                document.querySelector(
                    ".notification-list"
                );

            if (!list)
                return;

            list.innerHTML = "";

            this.notifications.forEach(item => {

                const li =
                    document.createElement("li");

                li.className =
                    "notification-item";

                li.innerHTML = `

                    <div class="notification-icon">
                        <i class="${item.icon}"></i>
                    </div>

                    <div class="notification-body">
                        <h6>${item.title}</h6>
                        <p>${item.message}</p>
                    </div>

                `;

                list.appendChild(li);

            });

            if (this.notificationBadge) {

                this.notificationBadge.textContent =
                    this.notifications.length;

            }

        }

        async loadRecentActivity() {

            try {

                const response =
                    await fetch(
                        "/api/activity"
                    );

                if (!response.ok)
                    return;

                const activity =
                    await response.json();

                this.renderActivity(activity);

            } catch (error) {

                console.error(error);

            }

        }

        renderActivity(items) {

            if (!this.activity)
                return;

            this.activity.innerHTML = "";

            items.forEach(item => {

                const div =
                    document.createElement("div");

                div.className =
                    "activity-item";

                div.innerHTML = `

                    <div class="activity-icon">
                        <i class="${item.icon}"></i>
                    </div>

                    <div class="activity-content">
                        <h6>${item.title}</h6>
                        <small>${item.time}</small>
                    </div>

                `;

                this.activity.appendChild(div);

            });

        }

        async loadSystemHealth() {

            try {

                const response =
                    await fetch(
                        "/api/system-health"
                    );

                if (!response.ok)
                    return;

                const health =
                    await response.json();

                this.updateHealth(health);

            } catch (error) {

                console.error(error);

            }

        }

        updateHealth(data) {

            Object.keys(data).forEach(key => {

                const progress =
                    document.querySelector(
                        `[data-health="${key}"]`
                    );

                if (!progress)
                    return;

                progress.style.width =
                    data[key] + "%";

            });

        }

        initializeSearch() {

            if (!this.search)
                return;

            this.search.addEventListener(

                "input",

                e => {

                    const value =
                        e.target.value
                        .toLowerCase();

                    this.filterCards(value);

                }

            );

        }

        filterCards(value) {

            document.querySelectorAll(

                ".dashboard-card"

            ).forEach(card => {

                const text =
                    card.innerText
                    .toLowerCase();

                card.style.display =
                    text.includes(value)
                        ? ""
                        : "none";

            });

        }

        exportDashboard(format = "pdf") {

            window.location =
                `/reports/export/${format}`;

        }

        initializeExportButtons() {

            document.querySelectorAll(

                "[data-export]"

            ).forEach(button => {

                button.addEventListener(

                    "click",

                    e => {

                        this.exportDashboard(

                            e.currentTarget.dataset.export

                        );

                    }

                );

            });

        }

        synchronizeTheme() {

            const theme =
                localStorage.getItem("theme");

            if (theme) {

                document.body.dataset.theme =
                    theme;

            }

        }

        registerKeyboardShortcuts() {

            document.addEventListener(

                "keydown",

                e => {

                    if (!e.ctrlKey)
                        return;

                    switch (e.key.toLowerCase()) {

                        case "r":

                            e.preventDefault();

                            this.refreshDashboard();

                            break;

                        case "f":

                            e.preventDefault();

                            this.search?.focus();

                            break;

                    }

                }

            );

        }
        initializeStatusWidgets() {

            this.updateDockerStatus();

            this.updateAWSStatus();

            this.updateSecurityScore();

        }

        async updateDockerStatus() {

            try {

                const response = await fetch("/api/docker/status");

                if (!response.ok)
                    return;

                const data = await response.json();

                const containerCount = document.querySelector(
                    "[data-docker='containers']"
                );

                const runningCount = document.querySelector(
                    "[data-docker='running']"
                );

                if (containerCount)
                    containerCount.textContent = data.total || 0;

                if (runningCount)
                    runningCount.textContent = data.running || 0;

            } catch (error) {

                console.error("Docker status:", error);

            }

        }

        async updateAWSStatus() {

            try {

                const response = await fetch("/api/aws/status");

                if (!response.ok)
                    return;

                const data = await response.json();

                document.querySelectorAll("[data-aws]").forEach(item => {

                    const key = item.dataset.aws;

                    if (data[key] !== undefined)
                        item.textContent = data[key];

                });

            } catch (error) {

                console.error("AWS status:", error);

            }

        }

        async updateSecurityScore() {

            try {

                const response = await fetch("/api/security/score");

                if (!response.ok)
                    return;

                const data = await response.json();

                const score = document.querySelector(
                    ".security-score-value"
                );

                const progress = document.querySelector(
                    ".security-score-progress"
                );

                if (score)
                    score.textContent = data.score + "%";

                if (progress)
                    progress.style.width = data.score + "%";

            } catch (error) {

                console.error(error);

            }

        }

        initializeCharts() {

            if (

                window.CloudShield &&
                window.CloudShield.Charts &&
                typeof window.CloudShield.Charts.init === "function"

            ) {

                window.CloudShield.Charts.init();

            }

        }

        showToast(message, type = "info") {

            if (

                window.CloudShield &&
                window.CloudShield.Toast

            ) {

                window.CloudShield.Toast.show(
                    message,
                    type
                );

            } else {

                console.log(message);

            }

        }

        handleResize() {

            document.body.classList.add("dashboard-resize");

            clearTimeout(this.resizeTimer);

            this.resizeTimer = setTimeout(() => {

                document.body.classList.remove(
                    "dashboard-resize"
                );

            }, 250);

        }

        handleVisibility() {

            if (document.hidden) {

                clearInterval(this.refreshTimer);

            } else {

                this.refreshDashboard();

                this.startAutoRefresh();

            }

        }

        destroy() {

            clearInterval(this.refreshTimer);

            window.removeEventListener(
                "resize",
                this.handleResize
            );

            document.removeEventListener(
                "visibilitychange",
                this.handleVisibility
            );

        }

        optimize() {

            if ("requestIdleCallback" in window) {

                requestIdleCallback(() => {

                    this.initializeStatusWidgets();

                    this.initializeCharts();

                    this.initializeExportButtons();

                    this.synchronizeTheme();

                    this.registerKeyboardShortcuts();

                });

            } else {

                this.initializeStatusWidgets();

                this.initializeCharts();

                this.initializeExportButtons();

                this.synchronizeTheme();

                this.registerKeyboardShortcuts();

            }

        }

    }

    document.addEventListener("DOMContentLoaded", () => {

        const dashboard = new Dashboard();

        dashboard.optimize();

        window.CloudShield =
            window.CloudShield || {};

        window.CloudShield.Dashboard =
            dashboard;

    });

})();