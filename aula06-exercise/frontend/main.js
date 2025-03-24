document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault()

    const movies = {
        name: document.querySelector('#name').value,
        rating: parseInt(document.querySelector('#rating').value),
        description: document.querySelector('#description').value
    };

    const res = await fetch("http://127.0.0.1:8000/filme", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(movies),
    });

    if (res.ok) {
        const data = await res.json();
        console.log(data);

        document.querySelector("#response").innerHTML = `
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Nome</th>
                        <th scope="col">Avaliação</th>
                        <th scope="col">Descrição</th>
                    </tr>

                    <tbody>
                        <tr>
                            <td>${data.filme.name}</td>
                            <td>${data.filme.rating}</td>
                            <td>${data.filme.description}</td>
                        </tr>
                    </tbody>
                </thead>
            </table>
        `;
    } else {
        console.error("Erro ao adicionar o filme:", res.statusText);
    }

    document.querySelector("form").reset();
})

document.querySelector('#all').addEventListener('click', async () => {
    const res = await fetch("http://127.0.0.1:8000/filmes");
    const movies = await res.json();

    document.querySelector("#response").innerHTML = `
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">Nome</th>
                    <th scope="col">Avaliação</th>
                    <th scope="col">Descrição</th>
                </tr>
            </thead>
            <tbody>
                ${movies.map(movie => `
                    <tr>
                        <td>${movie.name}</td>
                        <td>${movie.rating}</td>
                        <td>${movie.description}</td>
                    </tr>
                `).join('')}  
            </tbody>
        </table>
    `;
});
