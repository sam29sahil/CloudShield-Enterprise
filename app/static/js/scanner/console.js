class ConsoleManager {

    append(message) {

        const consoleBox = document.getElementById("live-console");

        if (!consoleBox) return;

        consoleBox.textContent += "\n" + message;

        consoleBox.scrollTop = consoleBox.scrollHeight;

    }

    clear() {

        const consoleBox = document.getElementById("live-console");

        if (!consoleBox) return;

        consoleBox.textContent = "";

    }

}

window.consoleManager = new ConsoleManager();

document
.getElementById("clear-console")
?.addEventListener("click", () => {

    window.consoleManager.clear();

});