from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = { 
    1: {"product": "Smartphone"},
    2: {"product": "TV"},
    3: {"product": "Carro"},
    4: {"product": "Moto"},
    5: {"product": "Videogame"},
    6: {"product": "Notebook"},
    7: {"product": "Tablet"},
    8: {"product": "Smartwatch"},
}

@app.get("/{id}")
def getProducts(id: int):
    return products.get(id, {"error": "Produto não encontrado"})