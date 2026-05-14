export function applyUI(element, data) {
    const risk = data.risk_level;

    element.style.transition = "all 0.3s ease";

    if (risk === "danger") {
        element.style.border = "2px solid red";
        element.style.backgroundColor = "#ffe6e6";
        injectLabel(element, "🚨 Danger");
    } else if (risk === "suspicious") {
        element.style.border = "2px solid orange";
        element.style.backgroundColor = "#fff4e6";
        injectLabel(element, "⚠️ Suspicious");
    }
}

function injectLabel(element, text) {
    if (element.querySelector(".guardianx-label")) return;

    const label = document.createElement("div");
    label.className = "guardianx-label";
    label.innerText = text;

    element.appendChild(label);
}