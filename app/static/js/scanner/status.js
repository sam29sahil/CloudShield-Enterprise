class StatusManager {

    update(data) {

        document.getElementById("scan-target").innerText =
            data.target || "--";

        document.getElementById("scan-tool").innerText =
            data.tool || "--";

        document.getElementById("scan-stage").innerText =
            data.message || "--";

        const badge = document.getElementById("scan-status-badge");

        badge.innerText = data.status;

        badge.className = "badge bg-primary";

        if (data.status === "Completed")
            badge.className = "badge bg-success";

        if (data.status === "Failed")
            badge.className = "badge bg-danger";

    }

}

window.statusManager = new StatusManager();