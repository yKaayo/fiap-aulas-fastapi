async function getProduct(maxValue, category) {
  document.querySelector("#response").innerHTML = ''

  const res = await fetch(
    `http://127.0.0.1:8000?maxValue=${maxValue}&category=${category}`
  );
  const data = await res.json();

  for (let key of Object.keys(data)) {
    console.log(data[key]);

    document.querySelector("#response").innerHTML += `
      <tr>
        <td>${data[key].product}</td>
        <td>${data[key].price}</td>
        <td>${data[key].category}</td>
      </tr>
    `
  }
}

const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(form);

  let maxValue;
  console.log(formData.get("maxValue"));

  formData.get("maxValue")
    ? (maxValue = formData.get("maxValue"))
    : (maxValue = null);

  const category = formData.get("category");

  getProduct(maxValue, category);
});
