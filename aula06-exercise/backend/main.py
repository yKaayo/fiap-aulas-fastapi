from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

listaFilme = []

class Filme(BaseModel):
 name: str
 rating: int
 description: str
    

@app.post("/filme")
def add_filme(filme: Filme):
    listaFilme.append(filme)
    return {"Message": "filme adicionado com sucesso!", "filme": filme}

@app.get("/filmes")
def get_filme():
    return listaFilme    
