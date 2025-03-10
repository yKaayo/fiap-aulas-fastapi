from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

users = [
    {"id": 1, "name": "Caio", "age": 19},
    {"id": 2, "name": "Douglas", "age": 19},
    {"id": 3, "name": "Emily", "age": 20},
    {"id": 4, "name": "Aline", "age": 20},
    {"id": 5, "name": "Thiago", "age": 18},
]

@app.get("/user", response_model=List[dict])
def search_user(name: Optional[str] = None, age: Optional[int] = None):
    result = users

    if name:
        result = [i for i in result if i["name"].lower() == name.lower()]

    if age:
        result = [i for i in result if i["age"] == age]

    return result