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

                }

            );

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

        }

    }

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

})();