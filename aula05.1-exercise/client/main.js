async function handleForm(e) {
  e.preventDefault();

  const task = {
    task: document.querySelector("#task").value,
    priority: parseInt(document.querySelector("#priority").value),
  };

  const res = await fetch("http://127.0.0.1:8000/task", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(task),
  });

  if (res.ok) {
    const data = await res.json();

    if (document.querySelector("#subtitle").textContent == "")
      document.querySelector("#subtitle").textContent = "Tarefas Cadastradas";

    document.querySelector("#tasks").innerHTML += `
        <div class='d-flex align-items-center bg-body-secondary rounded shadow-md'>
            <p class='mx-3 my-2 fs-4 fw-medium'>${data.task.task} - Prioridade ${data.task.priority}</p>
        </div>
    `;
  } else {
    console.error("Failed to add task:", res.statusText);
  }

  document.querySelector("form").reset();
}
