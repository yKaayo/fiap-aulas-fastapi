async function createProduct(e) {
  e.preventDefault();

  const form = document.querySelector("#form");

  const product = {
    name: document.querySelector("#name").value,
    price: parseFloat(document.querySelector("#price").value).toFixed(2),
    category: document.querySelector("#category").value,
  };

  const res = await fetch("http://127.0.0.1:8000/product", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(product),
  });

  const result = await res.json();
  console.log(result);

  document.querySelector("#result").innerHTML = `<p class="text-2xl">${result.message}</p>`;

  form.reset();
}

async function getProducts() {
  const res = await fetch("http://127.0.0.1:8000/products");
  const products = await res.json();
  console.log(products);

  document.querySelector("#result").innerHTML = products
    .map(
      (product) =>
        `<p class="text-2xl">${product.name} | ${product.price} | ${product.category}</p>`
    )
    .join("");
}
