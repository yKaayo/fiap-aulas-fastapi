from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = []

class Product(BaseModel):
    name: str
    price: float
    category: str

@app.post("/product")
def create_product(product: Product):
    products.append(product)
    return {"message": "Produto criado com sucesso!", "product": product}

@app.get("/products")
def get_products():
    return products
