/*
=========================================================
 CloudShield Enterprise
 charts.js
 Enterprise Chart Manager
=========================================================
*/

(function () {

    "use strict";

    class ChartManager {

        constructor() {

            this.charts = {};

            this.colors = {

                primary: "#4f8cff",
                success: "#22c55e",
                warning: "#f59e0b",
                danger: "#ef4444",
                info: "#06b6d4",
                secondary: "#64748b"

            };

            this.init();

        }

        init() {

            this.initializeDefaults();

            this.initializeDashboardCharts();

            this.initializeScannerCharts();

            this.initializeRiskCharts();

            this.initializeAssetCharts();

        }

        initializeDefaults() {

            if (typeof Chart === "undefined")
                return;

            Chart.defaults.font.family =
                "Inter, sans-serif";

            Chart.defaults.color =
                "#94a3b8";

            Chart.defaults.plugins.legend.position =
                "bottom";

            Chart.defaults.responsive = true;

            Chart.defaults.maintainAspectRatio = false;

        }

        initializeDashboardCharts() {

            this.securityScoreChart();

            this.scanHistoryChart();

            this.vulnerabilityChart();

        }

        securityScoreChart() {

            const canvas =
                document.getElementById("securityScoreChart");

            if (!canvas)
                return;

            this.charts.security = new Chart(canvas, {

                type: "doughnut",

                data: {

                    labels: [

                        "Secure",

                        "Risk"

                    ],

                    datasets: [{

                        data: [85, 15],

                        backgroundColor: [

                            this.colors.success,

                            this.colors.danger

                        ],

                        borderWidth: 0

                    }]

                },

                options: {

                    cutout: "75%",

                    plugins: {

                        legend: {

                            display: false

                        }

                    }

                }

            });

        }

        scanHistoryChart() {

            const canvas =
                document.getElementById("scanHistoryChart");

            if (!canvas)
                return;

            this.charts.history = new Chart(canvas, {

                type: "line",

                data: {

                    labels: [

                        "Mon",

                        "Tue",

                        "Wed",

                        "Thu",

                        "Fri",

                        "Sat",

                        "Sun"

                    ],

                    datasets: [{

                        label: "Scans",

                        data: [

                            5,

                            7,

                            4,

                            8,

                            9,

                            12,

                            10

                        ],

                        borderColor:

                            this.colors.primary,

                        tension: .4,

                        fill: true

                    }]

                },

                options: {

                    plugins: {

                        legend: {

                            display: false

                        }

                    }

                }

            });

        }

        vulnerabilityChart() {

            const canvas =
                document.getElementById("vulnerabilityChart");

            if (!canvas)
                return;

            this.charts.vulnerabilities = new Chart(canvas, {

                type: "bar",

                data: {

                    labels: [

                        "Critical",

                        "High",

                        "Medium",

                        "Low"

                    ],

                    datasets: [{

                        data: [

                            2,

                            6,

                            12,

                            18

                        ],

                        backgroundColor: [

                            this.colors.danger,

                            "#fb7185",

                            this.colors.warning,

                            this.colors.success

                        ]

                    }]

                },

                options: {

                    plugins: {

                        legend: {

                            display: false

                        }

                    }

                }

            });

        }
                initializeScannerCharts() {

            this.scanDurationChart();

            this.findingsTimelineChart();

            this.dockerChart();

            this.awsChart();

        }

        initializeRiskCharts() {

            this.riskTrendChart();

        }

        initializeAssetCharts() {

            this.assetDistributionChart();

        }

        assetDistributionChart() {

            const canvas =
                document.getElementById("assetDistributionChart");

            if (!canvas)
                return;

            this.charts.assets = new Chart(canvas, {

                type: "pie",

                data: {

                    labels: [

                        "Servers",

                        "Web Apps",

                        "Databases",

                        "Cloud",

                        "Network"

                    ],

                    datasets: [{

                        data: [

                            18,

                            12,

                            6,

                            10,

                            8

                        ],

                        backgroundColor: [

                            this.colors.primary,

                            this.colors.success,

                            this.colors.warning,

                            this.colors.info,

                            this.colors.secondary

                        ],

                        borderWidth: 0

                    }]

                }

            });

        }

        riskTrendChart() {

            const canvas =
                document.getElementById("riskTrendChart");

            if (!canvas)
                return;

            this.charts.risk = new Chart(canvas, {

                type: "line",

                data: {

                    labels: [

                        "Jan",

                        "Feb",

                        "Mar",

                        "Apr",

                        "May",

                        "Jun"

                    ],

                    datasets: [{

                        label: "Risk Score",

                        data: [

                            82,

                            78,

                            75,

                            71,

                            65,

                            60

                        ],

                        borderColor:
                            this.colors.danger,

                        backgroundColor:
                            "rgba(239,68,68,.15)",

                        fill: true,

                        tension: .35

                    }]

                }

            });

        }

        dockerChart() {

            const canvas =
                document.getElementById("dockerChart");

            if (!canvas)
                return;

            this.charts.docker = new Chart(canvas, {

                type: "bar",

                data: {

                    labels: [

                        "Running",

                        "Stopped",

                        "Paused"

                    ],

                    datasets: [{

                        data: [

                            8,

                            2,

                            1

                        ],

                        backgroundColor: [

                            this.colors.success,

                            this.colors.warning,

                            this.colors.secondary

                        ]

                    }]

                },

                options: {

                    plugins: {

                        legend: {

                            display: false

                        }

                    }

                }

            });

        }

        awsChart() {

            const canvas =
                document.getElementById("awsChart");

            if (!canvas)
                return;

            this.charts.aws = new Chart(canvas, {

                type: "polarArea",

                data: {

                    labels: [

                        "EC2",

                        "S3",

                        "IAM",

                        "Lambda",

                        "RDS"

                    ],

                    datasets: [{

                        data: [

                            5,

                            12,

                            18,

                            4,

                            3

                        ],

                        backgroundColor: [

                            this.colors.primary,

                            this.colors.success,

                            this.colors.warning,

                            this.colors.info,

                            this.colors.danger

                        ]

                    }]

                }

            });

        }

        scanDurationChart() {

            const canvas =
                document.getElementById("scanDurationChart");

            if (!canvas)
                return;

            this.charts.duration = new Chart(canvas, {

                type: "line",

                data: {

                    labels: [

                        "1",

                        "2",

                        "3",

                        "4",

                        "5",

                        "6"

                    ],

                    datasets: [{

                        label: "Minutes",

                        data: [

                            3,

                            5,

                            8,

                            6,

                            9,

                            7

                        ],

                        borderColor:
                            this.colors.info,

                        fill: false,

                        tension: .4

                    }]

                }

            });

        }

        findingsTimelineChart() {

            const canvas =
                document.getElementById("findingsTimelineChart");

            if (!canvas)
                return;

            this.charts.timeline = new Chart(canvas, {

                type: "bar",

                data: {

                    labels: [

                        "09:00",

                        "09:10",

                        "09:20",

                        "09:30",

                        "09:40"

                    ],

                    datasets: [{

                        label: "Findings",

                        data: [

                            2,

                            4,

                            7,

                            5,

                            3

                        ],

                        backgroundColor:
                            this.colors.warning

                    }]

                },

                options: {

                    plugins: {

                        legend: {

                            display: false

                        }

                    }

                }

            });

        }

        updateChart(name, labels, values) {

            const chart =
                this.charts[name];

            if (!chart)
                return;

            chart.data.labels = labels;

            chart.data.datasets[0].data = values;

            chart.update();

        }

        refreshAll() {

            Object.values(this.charts)

                .forEach(chart => {

                    chart.update();

                });

        }
        async loadChartData(endpoint, chartName) {

            try {

                const response = await fetch(endpoint);

                if (!response.ok)
                    return;

                const data = await response.json();

                this.updateChart(
                    chartName,
                    data.labels || [],
                    data.values || []
                );

            } catch (error) {

                console.error(
                    `Failed to load ${chartName}:`,
                    error
                );

            }

        }

        async refreshFromAPI() {

            await Promise.all([

                this.loadChartData(
                    "/api/dashboard/security-chart",
                    "security"
                ),

                this.loadChartData(
                    "/api/dashboard/history-chart",
                    "history"
                ),

                this.loadChartData(
                    "/api/dashboard/risk-chart",
                    "risk"
                ),

                this.loadChartData(
                    "/api/dashboard/assets-chart",
                    "assets"
                ),

                this.loadChartData(
                    "/api/dashboard/docker-chart",
                    "docker"
                ),

                this.loadChartData(
                    "/api/dashboard/aws-chart",
                    "aws"
                )

            ]);

        }

        applyTheme(theme = "dark") {

            const dark =
                theme === "dark";

            Chart.defaults.color =
                dark ? "#cbd5e1" : "#334155";

            Object.values(this.charts).forEach(chart => {

                if (!chart)
                    return;

                chart.options.plugins =
                    chart.options.plugins || {};

                chart.options.plugins.legend =
                    chart.options.plugins.legend || {};

                chart.options.plugins.legend.labels =
                    chart.options.plugins.legend.labels || {};

                chart.options.plugins.legend.labels.color =
                    Chart.defaults.color;

                chart.update();

            });

        }

        resizeCharts() {

            Object.values(this.charts).forEach(chart => {

                if (chart)
                    chart.resize();

            });

        }

        destroyCharts() {

            Object.values(this.charts).forEach(chart => {

                if (chart)
                    chart.destroy();

            });

            this.charts = {};

        }

        exportChart(chartName) {

            const chart =
                this.charts[chartName];

            if (!chart)
                return;

            const link =
                document.createElement("a");

            link.download =
                `${chartName}.png`;

            link.href =
                chart.toBase64Image();

            link.click();

        }

        initializeEvents() {

            window.addEventListener(

                "resize",

                () => this.resizeCharts()

            );

            document.addEventListener(

                "themeChanged",

                e => {

                    this.applyTheme(

                        e.detail.theme

                    );

                }

            );

        }

        startAutoRefresh() {

            setInterval(() => {

                this.refreshFromAPI();

            }, 60000);

        }

        optimize() {

            if ("requestIdleCallback" in window) {

                requestIdleCallback(() => {

                    this.initializeEvents();

                    this.startAutoRefresh();

                });

            } else {

                this.initializeEvents();

                this.startAutoRefresh();

            }

        }

    }

    document.addEventListener("DOMContentLoaded", () => {

        const charts =
            new ChartManager();

        charts.optimize();

        window.CloudShield =
            window.CloudShield || {};

        window.CloudShield.Charts = {

            manager: charts,

            init: () => charts.initializeDashboardCharts(),

            initScannerCharts: () =>
                charts.initializeScannerCharts(),

            refresh: () =>
                charts.refreshAll(),

            destroy: () =>
                charts.destroyCharts(),

            export: name =>
                charts.exportChart(name)

        };

    });

})();