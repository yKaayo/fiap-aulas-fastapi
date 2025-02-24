from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_index():
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    if not os.path.exists(file_path):
        return HTMLResponse(content= f"""
            <main class="container mx-auto px-5 sm:px-0">
                <div class="min-h-svh text-white flex flex-col items-center justify-center">
                    <h1 class="font-bold text-4xl text-center text-balance">Erro 404: index.html não encontrado</h1>  
                </div>
            </main>
        """, status_code=404)
                            

    with open(file_path, "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

@app.get("/product/{name}/{price}/{quantity}", response_class=HTMLResponse)
def exibir_dados(name: str, price: float, quantity: int):
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head lang="pt-BR">
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>DADOS DO PRODUTO</title>
        </head>
        <body class="bg-slate-600">
            <main class="container mx-auto px-5 sm:px-0">
                <div class="min-h-svh text-white w-full flex flex-col justify-center items-center gap-5">
                    <h2 class="font-bold text-4xl text-center text-balance">Produto cadastrado com sucesso!</h2>

                    <div class="w-fit flex flex-col gap-3">
                        <p class="font-semibold text-2xl">Nome do Produto: {name}</p>
                        <p class="font-semibold text-2xl">Preço: R${price:.2f}</p>
                        <p class="font-semibold text-2xl">Quantidade: {quantity}</p>
                    </div>

                    <a href="/" class="border-2 border-white font-bold text-2xl py-2 mt-3 duration-300 hover:bg-white hover:text-black rounded-2xl cursor-pointer px-5 py-2 text-center w-full hover:scale-105">Voltar</a>
                </div>
            </main>

            <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
