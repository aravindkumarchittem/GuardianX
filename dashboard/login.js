async function login() {
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value;
  const errorEl  = document.getElementById("error");

  errorEl.classList.remove("show");

  if (!username || !password) {
    errorEl.textContent = "Please enter both username and password.";
    errorEl.classList.add("show");
    return;
  }

  const btn = document.querySelector(".auth-submit");
  btn.disabled = true;
  btn.textContent = "Signing in…";

  try {
    const res  = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.status === "success") {
      localStorage.setItem("loggedIn", "true");
      window.location.href = "index.html";
    } else {
      errorEl.textContent = "Invalid credentials. Please try again.";
      errorEl.classList.add("show");
      btn.disabled = false;
      btn.textContent = "🔐 Sign In";
    }
  } catch {
    errorEl.textContent = "Could not reach the server. Is the backend running?";
    errorEl.classList.add("show");
    btn.disabled = false;
    btn.textContent = "🔐 Sign In";
  }
}

// Allow Enter key to submit
document.addEventListener("keydown", e => {
  if (e.key === "Enter") login();
});



// async function login() {
//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;

//     const res = await fetch("http://127.0.0.1:5000/login", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ username, password })
//     });

//     const data = await res.json();

//     if (data.status === "success") {
//         localStorage.setItem("loggedIn", "true");
//         window.location.href = "index.html";
//     } else {
//         document.getElementById("error").innerText = "Invalid credentials";
//     }
// }