<<<<<<< HEAD
/*
=========================================================
 CloudShield Enterprise
 scanner.js
 Universal Scanner Controller
=========================================================
*/

(function () {

    "use strict";

    const CS = window.CloudShield || {};

    class Scanner {

        constructor() {

            this.scanId = null;
            this.scanRunning = false;
            this.refreshInterval = 3000;
            this.refreshTimer = null;

            this.results = [];
            this.findings = [];

            this.init();

        }

        init() {

            this.cacheDOM();

            this.bindEvents();

            this.initializeTargetValidation();

            this.initializeToolSelection();

            this.initializeProfileSelection();

            this.initializeHistory();

            this.initializeFilters();

        }

        cacheDOM() {

            this.form =
                document.querySelector("#scanForm");

            this.target =
                document.querySelector("#target");

            this.profile =
                document.querySelector("#profile");

            this.toolList =
                document.querySelectorAll(".tool-checkbox");

            this.scanButton =
                document.querySelector("#startScan");

            this.cancelButton =
                document.querySelector("#cancelScan");

            this.progress =
                document.querySelector(".scan-progress");

            this.progressBar =
                document.querySelector(".progress-bar");

            this.logWindow =
                document.querySelector(".terminal-output");

            this.resultsTable =
                document.querySelector("#resultsTable tbody");

        }

        bindEvents() {

            if (this.form) {

                this.form.addEventListener(

                    "submit",

                    this.startScan.bind(this)

                );

            }

            if (this.cancelButton) {

                this.cancelButton.addEventListener(

                    "click",

                    this.cancelScan.bind(this)

                );

            }

        }

        initializeTargetValidation() {

            if (!this.target)
                return;

            this.target.addEventListener(

                "input",

                () => {

                    const value =
                        this.target.value.trim();

                    this.validateTarget(value);
=======
/* ==========================================================
   CloudShield Enterprise
   Universal Scanner
========================================================== */

"use strict";

window.CloudShield = window.CloudShield || {};

CloudShield.Scanner = (function () {

    let scanId = null;

    let polling = null;

    let elapsed = 0;

    let profile = "basic";

    let category = "web";

    let running = false;

    /* =====================================================
       Cache
    ===================================================== */

    const ui = {};

    /* =====================================================
       Init
    ===================================================== */

    function init() {

        cache();

        bindProfileCards();

        bindCategoryCards();

        bindButtons();

        resetDashboard();

        console.log(

            "CloudShield Scanner Initialized"

        );

    }

    /* =====================================================
       Cache Elements
    ===================================================== */

    function cache(){

        ui.form =

            document.getElementById("scanForm");

        ui.progressBar =

            document.getElementById("scanProgressBar");

        ui.progressValue =

            document.getElementById("progressPercent");

        ui.statusBadge =

            document.getElementById("scanStatusBadge");

        ui.currentTool =

            document.getElementById("currentTool");

        ui.currentStatus =

            document.getElementById("currentStatus");

        ui.elapsed =

            document.getElementById("elapsedTime");

        ui.remaining =

            document.getElementById("remainingTime");

        ui.feed =

            document.getElementById("activityFeed");

    }

    /* =====================================================
       Reset Dashboard
    ===================================================== */

    function resetDashboard(){

        updateProgress(0);

        setStatus("Ready","secondary");

        updateTool("Waiting");

        updateElapsed("00:00");

        updateRemaining("--:--");

    }

    /* =====================================================
       Profile Cards
    ===================================================== */

    function bindProfileCards(){

        const cards =

            document.querySelectorAll(

                ".profile-card"

            );

        cards.forEach(card=>{

            card.addEventListener(

                "click",

                function(){

                    cards.forEach(

                        c=>c.classList.remove("active")

                    );

                    this.classList.add("active");

                    profile =

                        this.dataset.profile;

                    document.getElementById(

                        "profile"

                    ).value = profile;

                    notify(

                        "Profile: "+profile,

                        "info"

                    );
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

                }

            );

<<<<<<< HEAD
        }

        validateTarget(target) {

            const regex =

                /^(https?:\/\/)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|localhost|(\d{1,3}\.){3}\d{1,3})/;

            if (!target.length) {

                this.target.classList.remove(

                    "is-valid",

                    "is-invalid"

                );

                return;

            }

            if (regex.test(target)) {

                this.target.classList.add("is-valid");

                this.target.classList.remove("is-invalid");

            } else {

                this.target.classList.add("is-invalid");

                this.target.classList.remove("is-valid");

            }

        }

        initializeToolSelection() {

            this.toolList.forEach(tool => {

                tool.addEventListener("change", () => {

                    this.updateSelectedTools();

                });

            });

        }

        updateSelectedTools() {

            const selected = [];

            this.toolList.forEach(tool => {

                if (tool.checked)

                    selected.push(tool.value);

            });

            const counter =
                document.querySelector("#toolCount");

            if (counter)

                counter.textContent =
                    selected.length;

        }

        initializeProfileSelection() {

            if (!this.profile)
                return;

            this.profile.addEventListener(

                "change",

                () => {

                    this.applyProfile();

                }

            );

        }

        applyProfile() {

            const profile =
                this.profile.value;

            this.toolList.forEach(tool => {

                tool.checked = false;

            });

            const profiles = {

                quick: [
                    "nmap",
                    "whatweb"
                ],

                standard: [
                    "nmap",
                    "whatweb",
                    "nikto",
                    "nuclei"
                ],

                full: [
                    "nmap",
                    "rustscan",
                    "whatweb",
                    "nikto",
                    "nuclei",
                    "ssl",
                    "waf",
                    "dnsrecon"
                ]

            };

            if (!profiles[profile])
                return;

            profiles[profile].forEach(name => {

                const tool =
                    document.querySelector(

                        `[value="${name}"]`

                    );

                if (tool)

                    tool.checked = true;

            });

            this.updateSelectedTools();

        }

        async startScan(event) {

            event.preventDefault();

            if (this.scanRunning)
                return;

            const payload = {

                target:
                    this.target.value,

                profile:
                    this.profile.value,

                tools:
                    this.getSelectedTools()

            };

            this.scanRunning = true;

            this.updateUI(true);

            try {

                const response =
                    await fetch(

                        "/security/start",

                        {

                            method: "POST",

                            headers: {

                                "Content-Type":
                                    "application/json"

                            },

                            body: JSON.stringify(
                                payload
                            )

                        }

                    );

                const data =
                    await response.json();

                this.scanId =
                    data.scan_id;

                this.startPolling();

            }

            catch (error) {

                console.error(error);

                this.scanRunning = false;

                this.updateUI(false);

            }

        }

        getSelectedTools() {

            const tools = [];

            this.toolList.forEach(tool => {

                if (tool.checked)

                    tools.push(tool.value);

            });

            return tools;

        }
        startPolling() {

            if (!this.scanId)
                return;

            this.refreshTimer = setInterval(() => {

                this.fetchStatus();

            }, this.refreshInterval);

        }

        stopPolling() {

            if (this.refreshTimer) {

                clearInterval(this.refreshTimer);

                this.refreshTimer = null;

            }

        }

        async fetchStatus() {

            try {

                const response = await fetch(
                    `/security/status/${this.scanId}`
                );

                if (!response.ok)
                    return;

                const data = await response.json();

                this.updateProgress(data);

                this.updateLogs(data.logs || []);

                this.updateTimeline(data.timeline || []);

                this.updateResults(data.results || []);

                this.updateFindings(data.findings || []);

                if (
                    data.status === "completed" ||
                    data.status === "failed" ||
                    data.status === "cancelled"
                ) {

                    this.finishScan(data);

                }

            } catch (error) {

                console.error(error);

            }

        }

        updateProgress(data) {

            const percent =
                Number(data.progress || 0);

            if (this.progressBar) {

                this.progressBar.style.width =
                    percent + "%";

                this.progressBar.textContent =
                    percent + "%";

            }

            const label =
                document.querySelector(".scan-status");

            if (label)
                label.textContent =
                    data.status || "Running";

        }

        updateLogs(logs) {

            if (!this.logWindow)
                return;

            this.logWindow.innerHTML = "";

            logs.forEach(log => {

                const line =
                    document.createElement("div");

                line.className = "terminal-line";

                line.textContent = log;

                this.logWindow.appendChild(line);

            });

            this.logWindow.scrollTop =
                this.logWindow.scrollHeight;

        }

        updateTimeline(events) {

            const timeline =
                document.querySelector(".scan-timeline");

            if (!timeline)
                return;

            timeline.innerHTML = "";

            events.forEach(event => {

                const item =
                    document.createElement("div");

                item.className = "timeline-item";

                item.innerHTML = `

                    <div class="timeline-dot"></div>

                    <div class="timeline-content">

                        <h6>${event.title}</h6>

                        <small>${event.time}</small>

                    </div>

                `;

                timeline.appendChild(item);

            });

        }

        updateResults(results) {

            this.results = results;

            if (!this.resultsTable)
                return;

            this.resultsTable.innerHTML = "";

            results.forEach(result => {

                const row =
                    document.createElement("tr");

                row.innerHTML = `

                    <td>${result.tool}</td>

                    <td>${result.target}</td>

                    <td>

                        <span class="badge bg-${this.statusColor(result.status)}">

                            ${result.status}

                        </span>

                    </td>

                    <td>${result.duration}</td>

                `;

                this.resultsTable.appendChild(row);

            });

        }

        updateFindings(findings) {

            this.findings = findings;

            const container =
                document.querySelector(".findings-list");

            if (!container)
                return;

            container.innerHTML = "";

            findings.forEach(item => {

                const card =
                    document.createElement("div");

                card.className =
                    "finding-card";

                card.innerHTML = `

                    <div class="severity severity-${item.severity.toLowerCase()}">

                        ${item.severity}

                    </div>

                    <h6>${item.title}</h6>

                    <p>${item.description}</p>

                `;

                container.appendChild(card);

            });

            this.updateRiskScore();

        }

        updateRiskScore() {

            const total =
                this.findings.length;

            let score = 100;

            this.findings.forEach(finding => {

                switch (finding.severity) {

                    case "Critical":
                        score -= 20;
                        break;

                    case "High":
                        score -= 10;
                        break;

                    case "Medium":
                        score -= 5;
                        break;

                    case "Low":
                        score -= 2;
                        break;

                }

            });

            score = Math.max(score, 0);

            const value =
                document.querySelector(".risk-score");

            const progress =
                document.querySelector(".risk-progress");

            if (value)
                value.textContent = score;

            if (progress)
                progress.style.width =
                    score + "%";

            const totalElement =
                document.querySelector(".finding-total");

            if (totalElement)
                totalElement.textContent = total;

        }

        statusColor(status) {

            switch ((status || "").toLowerCase()) {

                case "completed":
                    return "success";

                case "running":
                    return "primary";

                case "failed":
                    return "danger";

                case "warning":
                    return "warning";

                default:
                    return "secondary";

            }

        }
        async cancelScan() {

            if (!this.scanId)
                return;

            try {

                await fetch(

                    `/security/cancel/${this.scanId}`,

                    {
                        method: "POST"
                    }

                );

                this.finishScan({

                    status: "cancelled"

                });

            } catch (error) {

                console.error(error);

            }

        }

        finishScan(data) {

            this.scanRunning = false;

            this.stopPolling();

            this.updateUI(false);

            const status =
                document.querySelector(".scan-status");

            if (status)
                status.textContent =
                    data.status;

            this.showSummary();

        }

        updateUI(running) {

            if (this.scanButton)
                this.scanButton.disabled = running;

            if (this.cancelButton)
                this.cancelButton.disabled = !running;

            if (running) {

                this.scanButton.innerHTML =
                    '<i class="fas fa-spinner fa-spin"></i> Scanning...';

            } else {

                this.scanButton.innerHTML =
                    '<i class="fas fa-play"></i> Start Scan';

            }

        }

        exportResults(format = "pdf") {

            if (!this.scanId)
                return;

            window.location =
                `/reports/export/${this.scanId}/${format}`;

        }

        initializeExportButtons() {

            document.querySelectorAll("[data-export]")

                .forEach(button => {

                    button.addEventListener("click", e => {

                        this.exportResults(

                            e.currentTarget.dataset.export

                        );

                    });

                });

        }

        initializeHistory() {

            document.querySelectorAll(".history-row")

                .forEach(row => {

                    row.addEventListener("click", () => {

                        const id =
                            row.dataset.scan;

                        if (id)

                            window.location =
                                `/security/history/${id}`;

                    });

                });

        }

        initializeFilters() {

            document.querySelectorAll("[data-filter]")

                .forEach(button => {

                    button.addEventListener("click", e => {

                        this.filterFindings(

                            e.currentTarget.dataset.filter

                        );

                    });

                });

        }

        filterFindings(level) {

            document.querySelectorAll(".finding-card")

                .forEach(card => {

                    if (

                        level === "all" ||

                        card.innerText
                            .toLowerCase()
                            .includes(level.toLowerCase())

                    ) {

                        card.style.display = "";

                    } else {

                        card.style.display = "none";

                    }

                });

        }

        initializeSearch() {

            const input =
                document.querySelector("#findingSearch");

            if (!input)
                return;

            input.addEventListener("input", e => {

                const value =
                    e.target.value.toLowerCase();

                document.querySelectorAll(".finding-card")

                    .forEach(card => {

                        card.style.display =

                            card.innerText
                                .toLowerCase()
                                .includes(value)

                                ? ""

                                : "none";

                    });

            });

        }

        sortResults(column) {

            this.results.sort((a, b) => {

                if (a[column] < b[column])
                    return -1;

                if (a[column] > b[column])
                    return 1;

                return 0;

            });

            this.updateResults(this.results);

        }

        initializeSorting() {

            document.querySelectorAll("[data-sort]")

                .forEach(header => {

                    header.addEventListener("click", e => {

                        this.sortResults(

                            e.currentTarget.dataset.sort

                        );

                    });

                });

        }

        showSummary() {

            const total =
                this.findings.length;

            const critical =
                this.findings.filter(

                    f => f.severity === "Critical"

                ).length;

            const high =
                this.findings.filter(

                    f => f.severity === "High"

                ).length;

            const medium =
                this.findings.filter(

                    f => f.severity === "Medium"

                ).length;

            const low =
                this.findings.filter(

                    f => f.severity === "Low"

                ).length;

            const summary =
                document.querySelector(".scan-summary");

            if (!summary)
                return;

            summary.innerHTML = `

                <div class="summary-card">

                    <h5>Scan Completed</h5>

                    <p>Total Findings: ${total}</p>

                    <p>Critical: ${critical}</p>

                    <p>High: ${high}</p>

                    <p>Medium: ${medium}</p>

                    <p>Low: ${low}</p>

                </div>

            `;

        }
        initializeKeyboardShortcuts() {

            document.addEventListener("keydown", e => {

                if (!e.ctrlKey)
                    return;

                switch (e.key.toLowerCase()) {

                    case "s":

                        e.preventDefault();

                        if (!this.scanRunning && this.form) {
                            this.form.requestSubmit();
                        }

                        break;

                    case "e":

                        e.preventDefault();

                        this.exportResults("pdf");

                        break;

                    case "j":

                        e.preventDefault();

                        this.exportResults("json");

                        break;

                    case "c":

                        e.preventDefault();

                        if (this.scanRunning) {
                            this.cancelScan();
                        }

                        break;

                }

            });

        }

        initializeCharts() {

            if (
                window.CloudShield &&
                window.CloudShield.Charts &&
                typeof window.CloudShield.Charts.initScannerCharts === "function"
            ) {

                window.CloudShield.Charts.initScannerCharts();

            }

        }

        synchronizeTheme() {

            const theme =
                localStorage.getItem("theme");

            if (theme) {

                document.body.dataset.theme = theme;

            }

        }

        autoRefreshHistory() {

            const history =
                document.querySelector(".history-table");

            if (!history)
                return;

            setInterval(() => {

                if (!this.scanRunning) {

                    window.location.reload();

                }

            }, 60000);

        }

        resetScanner() {

            this.scanId = null;

            this.scanRunning = false;

            this.results = [];

            this.findings = [];

            this.stopPolling();

            if (this.progressBar) {

                this.progressBar.style.width = "0%";

                this.progressBar.textContent = "0%";

            }

            if (this.logWindow)
                this.logWindow.innerHTML = "";

            if (this.resultsTable)
                this.resultsTable.innerHTML = "";

        }

        optimize() {

            if ("requestIdleCallback" in window) {

                requestIdleCallback(() => {

                    this.initializeExportButtons();

                    this.initializeSearch();

                    this.initializeSorting();

                    this.initializeKeyboardShortcuts();

                    this.initializeCharts();

                    this.synchronizeTheme();

                    this.autoRefreshHistory();

                });

            } else {

                this.initializeExportButtons();

                this.initializeSearch();

                this.initializeSorting();

                this.initializeKeyboardShortcuts();

                this.initializeCharts();

                this.synchronizeTheme();

                this.autoRefreshHistory();

            }

        }

        destroy() {

            this.stopPolling();

            clearInterval(this.refreshTimer);
=======
        });

    }

    /* =====================================================
       Category
    ===================================================== */

    function bindCategoryCards(){

        const cards =

            document.querySelectorAll(

                ".category-card"

            );

        cards.forEach(card=>{

            card.onclick=function(){

                cards.forEach(

                    c=>c.classList.remove("active")

                );

                this.classList.add("active");

                category=this.dataset.category;

                document.getElementById(

                    "category"

                ).value=category;

                notify(

                    "Category: "+category,

                    "success"

                );

            };

        });

    }

    /* =====================================================
       Buttons
    ===================================================== */

    function bindButtons(){

        if(!ui.form)

            return;

        ui.form.addEventListener(

            "submit",

            onSubmit

        );

    }

    /* =====================================================
       Submit
    ===================================================== */

    function onSubmit(e){

        running=true;

        elapsed=0;

        startTimer();

        addActivity(

            "Starting Enterprise Scan..."

        );

        setStatus(

            "Running",

            "primary"

        );

    }

    /* =====================================================
       Timer
    ===================================================== */

    function startTimer(){

        clearInterval(polling);

        polling=setInterval(function(){

            elapsed++;

            let m=Math.floor(elapsed/60);

            let s=elapsed%60;

            updateElapsed(

                pad(m)+":"+pad(s)

            );

        },1000);

    }

    function stopTimer(){

        clearInterval(

            polling

        );

    }

    function pad(v){

        return v<10

            ? "0"+v

            : v;

    }

    /* =====================================================
       Progress
    ===================================================== */

    function updateProgress(percent){

        if(ui.progressBar)

            ui.progressBar.style.width=

                percent+"%";

        if(ui.progressValue)

            ui.progressValue.innerHTML=

                percent+"%";

    }

    /* =====================================================
       Status
    ===================================================== */

    function setStatus(text,color){

        if(!ui.statusBadge)

            return;

        ui.statusBadge.className=

            "badge bg-"+color;

        ui.statusBadge.innerHTML=text;

    }

    /* =====================================================
       Tool
    ===================================================== */

    function updateTool(tool){

        if(ui.currentTool)

            ui.currentTool.innerHTML=tool;

    }

    /* =====================================================
       Time
    ===================================================== */

    function updateElapsed(value){

        if(ui.elapsed)

            ui.elapsed.innerHTML=value;

    }

    function updateRemaining(value){

        if(ui.remaining)

            ui.remaining.innerHTML=value;

    }

    /* =====================================================
       Feed
    ===================================================== */

    function addActivity(message){

        if(!ui.feed)

            return;

        let div=

            document.createElement("div");

        div.className=

            "activity-item";

        div.innerHTML=

            '<i class="fas fa-circle text-success"></i> '

            +message;

        ui.feed.prepend(div);

    }

    /* =====================================================
       Notification
    ===================================================== */

    function notify(msg,type){

        console.log(

            "["+type+"]",

            msg

        );

    }

    /* =====================================================
       Public
    ===================================================== */

    return{

        init,

        updateProgress,

        updateTool,

        addActivity,

        notify,

        setStatus,

        stopTimer

    };

})();

document.addEventListener(

    "DOMContentLoaded",

    function(){

        if(

            CloudShield.Scanner

        ){

            CloudShield.Scanner.init();
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        }

    }

<<<<<<< HEAD
    document.addEventListener("DOMContentLoaded", () => {

        const scanner = new Scanner();

        scanner.optimize();

        window.CloudShield =
            window.CloudShield || {};

        window.CloudShield.Scanner =
            scanner;

    });
=======
);
/* ==========================================================
   LIVE PROGRESS ENGINE
========================================================== */

(function(){

    let liveInterval = null;

    function startPolling(id){

        scanId = id;

        if(liveInterval){

            clearInterval(liveInterval);

        }

        liveInterval = setInterval(fetchProgress,1500);

    }

    async function fetchProgress(){

        if(!scanId){

            return;

        }

        try{

            const response = await fetch(

                `/scanner/progress/${scanId}`

            );

            if(!response.ok){

                throw new Error("Polling failed");

            }

            const data = await response.json();

            if(!data.success){

                return;

            }

            updateLiveDashboard(data.data);

        }

        catch(error){

            console.error(error);

        }

    }

    function stopPolling(){

        clearInterval(liveInterval);

    }

    /* ========================================= */

    function updateLiveDashboard(progress){

        if(progress.percent!==undefined){

            updateProgress(progress.percent);

        }

        if(progress.current_tool){

            updateTool(progress.current_tool);

            updateTimeline(progress.current_tool);

        }

        if(progress.status){

            setStatus(

                progress.status,

                progress.status==="Completed"

                    ? "success"

                    : "primary"

            );

        }

        if(progress.message){

            addActivity(

                progress.message

            );

        }

        if(progress.status==="Completed"){

            completeScan(progress);

        }

    }

    function completeScan(progress){

        stopPolling();

        stopTimer();

        updateProgress(100);

        setStatus(

            "Completed",

            "success"

        );

        animateScore(

            progress.score || 100

        );

        notify(

            "Enterprise Scan Completed",

            "success"

        );

    }

    /* ========================================= */

    CloudShield.Scanner.startPolling =

        startPolling;

})();
/* ==========================================================
   TIMELINE ENGINE
========================================================== */

(function(){

    function updateTimeline(tool){

        const items =

            document.querySelectorAll(

                ".timeline-item"

            );

        items.forEach(function(item){

            const current =

                item.dataset.tool;

            item.classList.remove(

                "running"

            );

            if(current===tool){

                item.classList.add(

                    "running"

                );

            }

        });

    }

    function completeTool(tool){

        const card =

            document.querySelector(

                `.timeline-item[data-tool="${tool}"]`

            );

        if(!card)

            return;

        card.classList.remove(

            "running"

        );

        card.classList.add(

            "completed"

        );

    }

    CloudShield.Scanner.updateTimeline=

        updateTimeline;

    CloudShield.Scanner.completeTool=

        completeTool;

})();
/* ==========================================================
   COUNTERS
========================================================== */

(function(){

    function animateCounter(

        element,

        target

    ){

        if(!element)

            return;

        let value = 0;

        const step =

            Math.max(

                1,

                Math.ceil(target/60)

            );

        const timer =

            setInterval(function(){

                value += step;

                if(value>=target){

                    value = target;

                    clearInterval(timer);

                }

                element.innerHTML=value;

            },20);

    }

    function animateScore(score){

        const node =

            document.getElementById(

                "securityScore"

            );

        animateCounter(

            node,

            score

        );

    }

    CloudShield.Scanner.animateScore=

        animateScore;

})();
/* ==========================================================
   PROGRESS RING
========================================================== */

(function(){

    function updateRing(percent){

        const ring =

            document.querySelector(

                ".progress-ring"

            );

        if(!ring)

            return;

        const degree =

            percent*3.6;

        ring.style.background =

            `radial-gradient(circle,#182338 60%,transparent 61%),
             conic-gradient(
                #2563EB ${degree}deg,
                #23324A ${degree}deg
             )`;

    }

    CloudShield.Scanner.updateRing=

        updateRing;

})();
/* ==========================================================
   REPORTS
========================================================== */

(function(){

    function bindReports(){

        document

            .querySelectorAll(

                ".report-card"

            )

            .forEach(function(card){

                card.onclick=function(){

                    notify(

                        "Generating report...",

                        "info"

                    );

                };

            });

    }

    bindReports();

})();
/* ==========================================================
   UTILITIES
========================================================== */

(function(){

    function scrollFeed(){

        const feed =

            document.getElementById(

                "activityFeed"

            );

        if(feed){

            feed.scrollTop=0;

        }

    }

    function flash(element){

        if(!element)

            return;

        element.classList.add(

            "flash"

        );

        setTimeout(function(){

            element.classList.remove(

                "flash"

            );

        },900);

    }

    CloudShield.Scanner.flash=

        flash;

    CloudShield.Scanner.scrollFeed=

        scrollFeed;

})();
/* ==========================================================
   ENTERPRISE AJAX SCAN ENGINE
========================================================== */

(function(){

    async function submitScan(e){

        if(e){

            e.preventDefault();

        }

        const form=document.getElementById("scanForm");

        if(!form){

            return;

        }

        const formData=new FormData(form);

        clearResults();

        CloudShield.Scanner.setStatus(
            "Initializing",
            "info"
        );

        CloudShield.Scanner.updateProgress(0);

        CloudShield.Scanner.addActivity(
            "Preparing security engine..."
        );

        try{

            const response=await fetch(

                form.action || window.location.href,

                {

                    method:"POST",

                    body:formData,

                    headers:{

                        "X-Requested-With":"XMLHttpRequest"

                    }

                }

            );

            const data=await response.json();

            if(!data.success){

                throw new Error(

                    data.error ||

                    "Scan failed"

                );

            }

            if(data.scan){

                CloudShield.Scanner.startPolling(

                    data.scan.id

                );

            }

            CloudShield.Scanner.notify(

                "Scan Started",

                "success"

            );

        }

        catch(error){

            CloudShield.Scanner.notify(

                error.message,

                "danger"

            );

            CloudShield.Scanner.setStatus(

                "Failed",

                "danger"

            );

            console.error(error);

        }

    }

    function clearResults(){

        document

            .querySelectorAll("pre")

            .forEach(function(pre){

                pre.textContent="";

            });

    }

    document

        .addEventListener(

            "DOMContentLoaded",

            function(){

                const form=

                    document.getElementById(

                        "scanForm"

                    );

                if(form){

                    form.removeEventListener(

                        "submit",

                        submitScan

                    );

                    form.addEventListener(

                        "submit",

                        submitScan

                    );

                }

            }

        );

})();
/* ==========================================================
   RESULT RENDERER
========================================================== */

(function(){

    function renderResults(result){

        if(!result){

            return;

        }

        renderSummary(result);

        renderFindings(result);

        renderOutputs(result);

    }

    function renderSummary(result){

        setText(

            "securityScore",

            result.score || 0

        );

        setText(

            "currentStatus",

            result.status || "Completed"

        );

    }

    function renderFindings(result){

        if(!result.findings){

            return;

        }

        const tbody=

            document.querySelector(

                ".findings-table tbody"

            );

        if(!tbody){

            return;

        }

        tbody.innerHTML="";

        result.findings.forEach(function(item){

            tbody.insertAdjacentHTML(

                "beforeend",

                createFinding(item)

            );

        });

    }

    function renderOutputs(result){

        if(result.outputs){

            Object.keys(result.outputs)

            .forEach(function(tool){

                const pre=

                    document.getElementById(

                        "output-"+tool

                    );

                if(pre){

                    pre.textContent=

                        result.outputs[tool];

                }

            });

        }

    }

    function createFinding(f){

        return `

<tr>

<td>

<span class="severity-badge severity-${(f.severity||'info').toLowerCase()}">

${f.severity||"Info"}

</span>

</td>

<td>${f.tool||"--"}</td>

<td>${f.category||"--"}</td>

<td>${f.title||"--"}</td>

<td>${f.cvss||"--"}</td>

<td>${f.status||"Open"}</td>

<td>

<button class="btn btn-sm btn-primary">

View

</button>

</td>

</tr>

`;

    }

    function setText(id,value){

        const el=document.getElementById(id);

        if(el){

            el.innerHTML=value;

        }

    }

    CloudShield.Scanner.renderResults=

        renderResults;

})();
/* ==========================================================
   TOAST NOTIFICATIONS
========================================================== */

(function(){

    function toast(message,type="info"){

        let container=

            document.getElementById(

                "toastContainer"

            );

        if(!container){

            container=document.createElement("div");

            container.id="toastContainer";

            container.style.position="fixed";

            container.style.top="25px";

            container.style.right="25px";

            container.style.zIndex="99999";

            document.body.appendChild(container);

        }

        const toast=document.createElement("div");

        toast.className=

            "alert alert-"+type;

        toast.style.minWidth="320px";

        toast.style.marginBottom="12px";

        toast.innerHTML=message;

        container.appendChild(toast);

        setTimeout(function(){

            toast.remove();

        },3500);

    }

    CloudShield.Scanner.notify=

        toast;

})();

/* ==========================================================
   SHORTCUTS
========================================================== */

(function(){

    document.addEventListener(

        "keydown",

        function(e){

            if(

                e.ctrlKey &&

                e.key==="Enter"

            ){

                const form=

                    document.getElementById(

                        "scanForm"

                    );

                if(form){

                    form.requestSubmit();

                }

            }

            if(

                e.key==="Escape"

            ){

                CloudShield.Scanner.stopTimer();

            }

        }

    );

})();
/* ==========================================================
   DASHBOARD REFRESH
========================================================== */

(function(){

    function refresh(){

        fetch("/security/api/dashboard")

        .then(r=>r.json())

        .then(function(data){

            if(data.score){

                CloudShield.Scanner.animateScore(

                    data.score

                );

            }

        })

        .catch(function(){});

    }

    setInterval(

        refresh,

        30000

    );

})();
/* ==========================================================
   ENTERPRISE CHARTS
========================================================== */

(function(){

    let charts={};

    function initCharts(){

        if(typeof Chart==="undefined"){

            return;

        }

        initSeverity();

        initRisk();

    }

    function initSeverity(){

        const canvas=document.getElementById("severityChart");

        if(!canvas){

            return;

        }

        charts.severity=new Chart(canvas,{

            type:"doughnut",

            data:{

                labels:[

                    "Critical",

                    "High",

                    "Medium",

                    "Low"

                ],

                datasets:[{

                    data:[0,0,0,0]

                }]

            },

            options:{

                responsive:true,

                plugins:{

                    legend:{

                        position:"bottom"

                    }

                }

            }

        });

    }

    function initRisk(){

        const canvas=document.getElementById("riskChart");

        if(!canvas){

            return;

        }

        charts.risk=new Chart(canvas,{

            type:"bar",

            data:{

                labels:["Risk"],

                datasets:[{

                    data:[0]

                }]

            },

            options:{

                responsive:true,

                plugins:{

                    legend:{

                        display:false

                    }

                }

            }

        });

    }

    function updateCharts(result){

        if(

            charts.severity &&

            result.summary

        ){

            charts.severity.data.datasets[0].data=[

                result.summary.critical||0,

                result.summary.high||0,

                result.summary.medium||0,

                result.summary.low||0

            ];

            charts.severity.update();

        }

    }

    CloudShield.Scanner.initCharts=initCharts;

    CloudShield.Scanner.updateCharts=updateCharts;

})();
/* ==========================================================
   SCAN QUEUE
========================================================== */

(function(){

    const queue=[];

    let busy=false;

    function enqueue(data){

        queue.push(data);

        process();

    }

    async function process(){

        if(busy){

            return;

        }

        if(queue.length===0){

            return;

        }

        busy=true;

        const next=queue.shift();

        CloudShield.Scanner.addActivity(

            "Queued Scan Started"

        );

        try{

            await fetch(

                next.url,

                next.options

            );

        }

        catch(e){

            console.error(e);

        }

        busy=false;

        process();

    }

    CloudShield.Scanner.queue=enqueue;

})();
/* ==========================================================
   OFFLINE DETECTOR
========================================================== */

(function(){

    function online(){

        CloudShield.Scanner.notify(

            "Connection Restored",

            "success"

        );

    }

    function offline(){

        CloudShield.Scanner.notify(

            "Offline Mode",

            "warning"

        );

    }

    window.addEventListener(

        "online",

        online

    );

    window.addEventListener(

        "offline",

        offline

    );

})();
/* ==========================================================
   PERFORMANCE MONITOR
========================================================== */

(function(){

    function monitor(){

        if(

            !window.performance

        ){

            return;

        }

        const memory=

            performance.memory;

        if(!memory){

            return;

        }

        const cpu=document.getElementById(

            "cpuUsage"

        );

        const ram=document.getElementById(

            "memoryUsage"

        );

        if(cpu){

            cpu.innerHTML="Normal";

        }

        if(ram){

            ram.innerHTML=

                Math.round(

                    memory.usedJSHeapSize/

                    1048576

                )+" MB";

        }

    }

    setInterval(

        monitor,

        3000

    );

})();
/* ==========================================================
   THEME HELPERS
========================================================== */

(function(){

    function dark(){

        document.body.classList.add(

            "scanner-dark"

        );

    }

    function light(){

        document.body.classList.remove(

            "scanner-dark"

        );

    }

    CloudShield.Scanner.dark=dark;

    CloudShield.Scanner.light=light;

})();
/* ==========================================================
   ERROR RECOVERY
========================================================== */

(function(){

    window.addEventListener(

        "error",

        function(e){

            console.error(e);

            CloudShield.Scanner.notify(

                "Unexpected Error",

                "danger"

            );

        }

    );

})();
/* ==========================================================
   AUTO RECONNECT
========================================================== */

(function(){

    let attempts=0;

    function reconnect(){

        attempts++;

        if(attempts>5){

            return;

        }

        CloudShield.Scanner.notify(

            "Reconnecting...",

            "warning"

        );

        setTimeout(function(){

            location.reload();

        },2000);

    }

    window.addEventListener(

        "offline",

        reconnect

    );
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

})();