class LiveScanner {

    constructor(scanId) {

        this.scanId = scanId;

        this.interval = null;

    }

    start() {

        this.interval = setInterval(() => {

            this.refresh();

        }, 1000);

    }

    stop() {

        clearInterval(this.interval);

    }

    async refresh() {

        try {

            const response = await fetch(

                `/scanner/progress/${this.scanId}`

            );

            const json = await response.json();

            if (!json.success) {

                return;

            }

            const data = json.data;

            window.progressManager.update(

                data.progress

            );

            window.statusManager.update(

                data

            );

            window.timerManager.update(

                data.elapsed

            );

            this.updateTimeline(

                data.status

            );

            if (

                data.status === "Completed" ||

                data.status === "Failed" ||

                data.status === "Cancelled"

            ) {

                this.stop();

            }

        }

        catch (e) {

            console.error(e);

        }

    }

    updateTimeline(status) {

        const stages = {

            "Validating Target":"stage-validation",

            "Initializing Tool":"stage-init",

            "Running":"stage-running",

            "Parsing Results":"stage-parsing",

            "Generating Findings":"stage-findings",

            "Generating Report":"stage-report",

            "Completed":"stage-complete"

        };

        Object.values(stages).forEach(id=>{

            const el=document.getElementById(id);

            if(el){

                el.classList.remove("active");

            }

        });

        const current=stages[status];

        if(current){

            document

                .getElementById(current)

                ?.classList.add("active");

        }

    }

}

const scanner = new LiveScanner(scanId);

scanner.start();