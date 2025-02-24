from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # Permite retornar respostas HTML
from fastapi.staticfiles import StaticFiles  # Serve arquivos estáticos (HTML, CSS, JS)
import os  # Biblioteca para manipulação de caminhos de arquivos

app = FastAPI()

# Servindo arquivos estáticos
# Montamos a pasta "static" para que o FastAPI possa servir arquivos estáticos como HTML, CSS, JS, imagens, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rota para carregar o index.html na URL raiz "/"
@app.get("/", response_class=HTMLResponse)
def serve_index():
    """
    Essa função retorna o conteúdo do arquivo index.html localizado na pasta 'static/'.
    Se o arquivo não for encontrado, retorna um erro 404.
    """
    file_path = os.path.join(os.getcwd(), "static", "index.html")  # Obtém o caminho absoluto do arquivo
    if not os.path.exists(file_path):  # Verifica se o arquivo existe
        return HTMLResponse(content="<h2>Erro 404: index.html não encontrado</h2>", status_code=404)

    with open(file_path, "r", encoding="utf-8") as file:  # Abre o arquivo e lê seu conteúdo
        return HTMLResponse(content=file.read())  # Retorna o HTML como resposta

# Exemplo de formulário e exibição de dados com Path Parameters
@app.get("/user/{nome}/{idade}", response_class=HTMLResponse)
def exibir_dados(nome: str, idade: int):
    html_content = f"""
    <html>
        <head><title>Dados do Usuário</title></head>
        <body>
            <h2>Dados Recebidos</h2>
            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>Idade:</strong> {idade}</p>
            <br>
            <a href="/">Voltar</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)  # Retorna o HTML formatado como resposta
