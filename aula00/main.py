from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/users")
def get_user():
    return {"name": "Caio"}

@app.get("/sum/{num1}/{num2}")
def sum(num1: int, num2: int):
    return {'First Number': num1, 'Second Number': num2, 'Sum': f'{num1 + num2}'}

@app.get("/par-impar/{num}")
def abc(num: int = 0):
    return {'Número': num, 'Categoria': f'O número {num} é par' if num % 2 == 0 else f'O número {num} é ímpar'}


# -- / -- / -- / -- / -- / -- / -- / --  


# Path
@app.get("/path/{id}")
def get_user(id: int):
    return {'id': id}

# Query
@app.get("/query")
def get_user(name: str = 'Não Informado', age: int = None):
    return {'name': name, 'idade': age}
