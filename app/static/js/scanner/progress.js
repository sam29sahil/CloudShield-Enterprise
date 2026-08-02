class ProgressManager {

    update(progress) {

        const bar = document.getElementById("scan-progress-bar");
        const text = document.getElementById("progress-text");

        if (!bar || !text) return;

        bar.style.width = progress + "%";
        bar.innerText = progress + "%";

        text.innerText = progress + "%";
    }

}

window.progressManager = new ProgressManager();