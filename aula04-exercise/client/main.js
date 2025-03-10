async function getProduct(id) {
  const res = await fetch(`http://127.0.0.1:8000/${id}`);
  const data = await res.json();

  if (!data.error) {
    return (document.querySelector(
      "#response"
    ).innerHTML = `O produto de ID ${data.id} é ${data.product}`);
  }

  document.querySelector("#response").innerHTML = data.error;
}

const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const id = formData.get("id");

  getProduct(id);
});
