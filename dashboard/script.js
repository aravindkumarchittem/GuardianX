const API_URL = "http://127.0.0.1:5000/get-flagged";

// 🔐 Auth guard
if (localStorage.getItem("loggedIn") !== "true") {
  window.location.href = "login.html";
}

let allMessages = [];

// ─── Theme ─────────────────────────────────────────────────
function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  const icon  = document.getElementById("themeIcon");
  const label = document.getElementById("themeLabel");
  if (theme === "light") {
    icon.textContent  = "🌙";
    label.textContent = "Dark Mode";
  } else {
    icon.textContent  = "☀️";
    label.textContent = "Light Mode";
  }
  localStorage.setItem("gx-theme", theme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute("data-theme");
  applyTheme(current === "dark" ? "light" : "dark");
}

// Restore saved theme
(function () {
  const saved = localStorage.getItem("gx-theme") || "dark";
  applyTheme(saved);
})();

// ─── Fetch & Render ─────────────────────────────────────────
async function fetchMessages() {
  showSkeletons();
  try {
    const res  = await fetch(API_URL);
    const data = await res.json();
    allMessages = data;
    updateStats(allMessages);
    renderMessages(allMessages);
  } catch (err) {
    showError();
  }
}

function updateStats(messages) {
  document.getElementById("statTotal").textContent     = messages.length;
  document.getElementById("statDanger").textContent    = messages.filter(m => m.risk_level === "danger").length;
  document.getElementById("statSuspicious").textContent= messages.filter(m => m.risk_level === "suspicious").length;
  document.getElementById("statSafe").textContent      = messages.filter(m => m.risk_level === "safe").length;
}

function renderMessages(messages) {
  const container = document.getElementById("messages-container");
  container.innerHTML = "";

  if (!messages.length) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">🔍</div>
        <p>No messages match this filter.</p>
      </div>`;
    return;
  }

  messages.forEach((msg, i) => {
    const level      = msg.risk_level || "safe";
    const score      = typeof msg.score === "number" ? msg.score : 0;
    const confidence = typeof msg.ml_confidence === "number" ? msg.ml_confidence : 0;

    // Derive fill class
    const fillClass  = level === "danger" ? "fill-danger"
                     : level === "suspicious" ? "fill-suspicious"
                     : "fill-safe";

    const badgeClass = level === "danger" ? "badge-danger"
                     : level === "suspicious" ? "badge-suspicious"
                     : "badge-safe";

    const riskIcon   = level === "danger" ? "🔴"
                     : level === "suspicious" ? "🟠"
                     : "🟢";

    const reasons    = Array.isArray(msg.reasons) ? msg.reasons : [];

    const div = document.createElement("div");
    div.className = `message-card ${level}`;
    div.style.animationDelay = `${i * 0.04}s`;

    div.innerHTML = `
      <div class="card-header">
        <div class="card-risk-badge ${badgeClass}">${riskIcon} ${level.toUpperCase()}</div>
      </div>
      <p class="card-message">${escapeHTML(msg.message)}</p>
      <div class="card-metrics">
        <div class="metric-item">
          <div class="metric-label">Risk Score</div>
          <div class="metric-value">${score}</div>
          <div class="meter-bar"><div class="meter-fill ${fillClass}" style="width:${Math.min(score, 100)}%"></div></div>
        </div>
        <div class="metric-item">
          <div class="metric-label">ML Confidence</div>
          <div class="metric-value">${(confidence * 100).toFixed(0)}%</div>
          <div class="meter-bar"><div class="meter-fill ${fillClass}" style="width:${Math.min(confidence * 100, 100)}%"></div></div>
        </div>
      </div>
      ${reasons.length ? `<div class="card-reasons">${reasons.map(r => `<span class="reason-tag">${escapeHTML(r)}</span>`).join("")}</div>` : ""}
    `;

    container.appendChild(div);
  });
}

function escapeHTML(str) {
  const div = document.createElement("div");
  div.appendChild(document.createTextNode(String(str)));
  return div.innerHTML;
}

function showSkeletons() {
  const container = document.getElementById("messages-container");
  container.innerHTML = Array(6).fill(0).map(() =>
    `<div class="skeleton" style="height:200px"></div>`
  ).join("");
}

function showError() {
  const container = document.getElementById("messages-container");
  container.innerHTML = `
    <div class="empty-state">
      <div class="empty-icon">⚠️</div>
      <p>Could not connect to the API. Is the backend running?</p>
    </div>`;
}

// ─── Filter ──────────────────────────────────────────────────
function filterMessages(type, btn) {
  // Update active button
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
  if (btn) btn.classList.add("active");

  const filtered = type === "all"
    ? allMessages
    : allMessages.filter(m => m.risk_level === type);

  renderMessages(filtered);
}

// ─── Auth ─────────────────────────────────────────────────────
function logout() {
  localStorage.removeItem("loggedIn");
  window.location.href = "login.html";
}

// ─── Init ─────────────────────────────────────────────────────
fetchMessages();




// const API_URL = "http://127.0.0.1:5000/get-flagged";

// // 🔐 Check login
// if (localStorage.getItem("loggedIn") !== "true") {
//     window.location.href = "login.html";
// }
// let allMessages = [];

// async function fetchMessages() {
//     const res = await fetch(API_URL);
//     const data = await res.json();

//     allMessages = data;
//     renderMessages(allMessages);
// }

// function renderMessages(messages) {
//     const container = document.getElementById("messages-container");
//     container.innerHTML = "";

//     messages.forEach(msg => {
//         const div = document.createElement("div");
//         div.className = `message-card ${msg.risk_level}`;

//         div.innerHTML = `
//             <p><strong>Message:</strong> ${msg.message}</p>
//             <p><strong>Risk:</strong> ${msg.risk_level}</p>
//             <p><strong>Score:</strong> ${msg.score}</p>
//             <p><strong>Confidence:</strong> ${msg.ml_confidence}</p>
//             <p><strong>Reasons:</strong> ${msg.reasons.join(", ")}</p>
//         `;

//         container.appendChild(div);
//     });
// }
// function logout() {
//     localStorage.removeItem("loggedIn");
//     window.location.href = "login.html";
// }
// function filterMessages(type) {
//     if (type === "all") {
//         renderMessages(allMessages);
//     } else {
//         const filtered = allMessages.filter(m => m.risk_level === type);
//         renderMessages(filtered);
//     }
// }

// fetchMessages();