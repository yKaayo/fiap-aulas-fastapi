function redirecionar(e) {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let price = document.getElementById("price").value;
    let quantity = document.getElementById("quantity").value;

    window.location.href = `/product/${name}/${price}/${quantity}`;
  }