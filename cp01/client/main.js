async function cadastrarFilme(e) {
  e.preventDefault();

  // Dados do form para enviar para Backend
  const movie = {
    title: document.querySelector("#title").value,
    description: document.querySelector("#description").value,
    genre: document.querySelector("#genre").value,
    release: document.querySelector("#release").value,
    image: document.querySelector("#image").value,
  };

  const res = await fetch("http://127.0.0.1:8000/movie", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(movie),
  })
  // Mantendo o usuário informado se deu certo
  if (!res.ok) {
      return document.querySelector('#info').textContent = 'Algo deu errado! O cadastro não ocorreu da forma esperada.'
  }

  document.querySelector('#info').textContent = 'Cadastrado com sucesso!'

  document.querySelector("form").reset();
}

async function getMovies() {
  const res = await fetch("http://127.0.0.1:8000/movies");
  const movies = await res.json();
  console.log(movies);

  document.querySelector('#data').innerHTML = ''
  movies.map(movie => document.querySelector('#data').innerHTML += `
  <div class="bg-gray-600/10 rounded-lg pb-3">
    <div class="w-full">
      <img src="${movie.image}" class="max-h-[350px] w-full cover">
    </div>

    <div class="flex flex-col px-5 mt-3">
      <h2 class="font-bold text-3xl">${movie.title}</h2>
      <p>${movie.description}</p>

      <div class="flex items-center justify-between">
        <p>${movie.genre}</p>
        <p>${movie.release}</p>
      </div>
    </div>
  </div>
  `
  )
}
