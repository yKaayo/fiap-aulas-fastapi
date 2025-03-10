function redirecionar(e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;

    window.location.href = `/user?name=${name}&age=${age}`;
  }