const registerForm = document.getElementById("registerForm");
const loginForm = document.getElementById("loginForm");

registerForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const user = {
    username: document.getElementById("regUsername").value,
    email: document.getElementById("regEmail").value,
    password: document.getElementById("regPassword").value,
  };

  const response = await fetch(
    "https://fiap-aula07-fastapi.up.railway.app/register",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    }
  );

  const data = await response.json();
  alert(data.message || data.detail);
  registerForm.reset();
});

loginForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const credentials = {
    username: document.getElementById("loginUsername").value,
    password: document.getElementById("loginPassword").value,
  };

  const response = await fetch(
    "https://fiap-aula07-fastapi.up.railway.app/login",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(credentials),
    }
  );

  const data = await response.json();
  alert(data.message || data.detail);
  loginForm.reset();
});
