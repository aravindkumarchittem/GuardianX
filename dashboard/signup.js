async function signup() {
  const username   = document.getElementById("username").value.trim();
  const password   = document.getElementById("password").value;
  const errorEl    = document.getElementById("errorMsg");
  const successEl  = document.getElementById("successMsg");

  errorEl.classList.remove("show");
  successEl.classList.remove("show");

  if (!username || !password) {
    errorEl.textContent = "Please fill in all fields.";
    errorEl.classList.add("show");
    return;
  }

  const btn = document.querySelector(".auth-submit");
  btn.disabled = true;
  btn.textContent = "Creating account…";

  try {
    const res  = await fetch("http://127.0.0.1:5000/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.status === "success") {
      successEl.textContent = data.message || "Account created! Redirecting…";
      successEl.classList.add("show");
      setTimeout(() => { window.location.href = "login.html"; }, 1500);
    } else {
      errorEl.textContent = data.message || "Signup failed. Please try again.";
      errorEl.classList.add("show");
      btn.disabled = false;
      btn.textContent = "✨ Create Account";
    }
  } catch {
    errorEl.textContent = "Could not reach the server. Is the backend running?";
    errorEl.classList.add("show");
    btn.disabled = false;
    btn.textContent = "✨ Create Account";
  }
}

document.addEventListener("keydown", e => {
  if (e.key === "Enter") signup();
});


// async function signup() {
//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;

//     const res = await fetch("http://127.0.0.1:5000/signup", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ username, password })
//     });

//     const data = await res.json();

//     document.getElementById("msg").innerText = data.message;

//     if (data.status === "success") {
//         window.location.href = "login.html";
//     }
// }