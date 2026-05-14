const API_URL = "http://127.0.0.1:5000/analyze-message";

const processedMessages = new Set();

function initObserver() {
    const chatContainer = document.querySelector("#main");

    if (!chatContainer) {
        console.log("Waiting for WhatsApp...");
        setTimeout(initObserver, 2000);
        return;
    }

    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                scanMessages();
            });
        });
    });

    observer.observe(chatContainer, {
        childList: true,
        subtree: true
    });

    console.log("GuardianX Running...");
}

function scanMessages() {
    // 🎯 ONLY CHAT AREA (important fix)
    const chatArea = document.querySelector("#main");

    if (!chatArea) return;

    const messages = chatArea.querySelectorAll("div[role='row']");

    messages.forEach((node) => {
        const spans = node.querySelectorAll("span");

        spans.forEach((span) => {
            const text = span.innerText.trim();

            // ✅ STRONG FILTER
            if (
                !text ||
                text.length < 5 ||
                text === "Today" ||
                text.includes("end-to-end encrypted") ||
                text.includes("Click to learn more") ||
                text.match(/^\d{1,2}:\d{2}$/) || // time
                text.length > 200 // avoid long system texts
            ) return;

            if (processedMessages.has(text)) return;

            processedMessages.add(text);

            console.log("🔥 FINAL MESSAGE:", text);

            // 🎯 Apply UI only inside chat area
            analyzeMessage(text, node);
        });
    });
}

async function analyzeMessage(message, node) {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        applyUI(node, data);

    } catch (err) {
        console.error("API Error:", err);
    }
}

function applyUI(node, data) {
    const risk = data.risk_level;

    node.style.transition = "0.3s";
    node.style.padding = "6px";
    node.style.borderRadius = "10px";

    if (risk === "danger") {
        node.style.border = "3px solid red";
        node.style.backgroundColor = "#ff4d4d";
        node.style.color = "white";
        addLabel(node, "🚨 DANGER");
    } 
    else if (risk === "suspicious") {
        node.style.border = "3px solid orange";
        node.style.backgroundColor = "#ffa500";
        node.style.color = "black";
        addLabel(node, "⚠️ SUSPICIOUS");
    }
}
function addLabel(node, text) {
    if (node.querySelector(".guardianx-label")) return;

    const label = document.createElement("div");
    label.className = "guardianx-label";
    label.innerText = text;

    node.appendChild(label);
}

setTimeout(initObserver, 3000);