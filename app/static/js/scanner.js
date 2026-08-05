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

                }

            );

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

        }

    }

    document.addEventListener("DOMContentLoaded", () => {

        const scanner = new Scanner();

        scanner.optimize();

        window.CloudShield =
            window.CloudShield || {};

        window.CloudShield.Scanner =
            scanner;

    });

})();