from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = { 
    1: {"product": "Smartphone", "price": 2000, "category": "eletronico"},
    2: {"product": "TV", "price": 2500, "category": "eletronico"},
    3: {"product": "Carro", "price": 40000, "category": "automovel"},
    4: {"product": "Moto", "price": 25000, "category": "automovel"},
    5: {"product": "Videogame", "price": 3000, "category": "eletronico"},
    6: {"product": "Notebook", "price": 3500, "category": "eletronico"},
    7: {"product": "Tablet", "price": 1500, "category": "eletronico"},
    8: {"product": "Smartwatch", "price": 1000, "category": "eletronico"},
}

@app.get("/")
def getProducts(maxValue: Optional[str] = None, category: Optional[str] = None):
    if maxValue == "null" and category == "null":
        return products
    elif maxValue == "null" and category != "null":
        newProducts = {}

        for i, product in products.items():
            if product["category"] == category:
                newProducts[i] = product

        return newProducts
    elif maxValue != "null" and category == "null":
        newProducts = {}

        for i, product in products.items():
            if product["price"] <= int(maxValue):
                newProducts[i] = product

        return newProducts
    else:
        newProducts = {}

        for i, product in products.items():
            if product["category"] == category and product["price"] <= int(maxValue):
                newProducts[i] = product

        return newProducts