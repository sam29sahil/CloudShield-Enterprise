/*
====================================
CloudShield Enterprise
Analytics Dashboard
====================================
*/

document.addEventListener("DOMContentLoaded", () => {

    const analytics = document.getElementById("analytics-data");

    if (!analytics) {

        console.error("Analytics data not found.");

        return;

    }

    // -----------------------------
    // Read data from Flask
    // -----------------------------

    const labels = JSON.parse(

        analytics.dataset.labels

    );

    const scores = JSON.parse(

        analytics.dataset.scores

    );

    const critical = Number(

        analytics.dataset.critical

    );

    const high = Number(

        analytics.dataset.high

    );

    const medium = Number(

        analytics.dataset.medium

    );

    const low = Number(

        analytics.dataset.low

    );

    initializeScoreChart(

        labels,

        scores

    );

    initializeSeverityChart(

        critical,

        high,

        medium,

        low

    );

});


// ====================================
// Security Score Trend
// ====================================

function initializeScoreChart(

    labels,

    scores

) {

    const canvas = document.getElementById(

        "scoreChart"

    );

    if (!canvas) return;

    new Chart(canvas, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "Security Score",

                    data: scores,

                    borderColor: "#0d6efd",

                    backgroundColor: "rgba(13,110,253,0.15)",

                    borderWidth: 3,

                    fill: true,

                    tension: 0.35,

                    pointRadius: 5,

                    pointHoverRadius: 7

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: true

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    max: 100,

                    ticks: {

                        stepSize: 10

                    }

                }

            }

        }

    });

}


// ====================================
// Severity Distribution
// ====================================

function initializeSeverityChart(

    critical,

    high,

    medium,

    low

) {

    const canvas = document.getElementById(

        "severityChart"

    );

    if (!canvas) return;

    new Chart(canvas, {

        type: "doughnut",

        data: {

            labels: [

                "Critical",

                "High",

                "Medium",

                "Low"

            ],

            datasets: [

                {

                    data: [

                        critical,

                        high,

                        medium,

                        low

                    ],

                    backgroundColor: [

                        "#212529",

                        "#dc3545",

                        "#ffc107",

                        "#0d6efd"

                    ],

                    borderWidth: 2

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "65%",

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}