class TimerManager {

    update(seconds) {

        const el = document.getElementById("scan-time");

        if (!el) return;

        el.innerText = seconds + " sec";

    }

}

window.timerManager = new TimerManager();