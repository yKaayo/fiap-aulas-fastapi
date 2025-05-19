from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext
from db import create_user, get_user_by_username

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

@app.post("/register")
def register_user(user: User):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")

    hashed_password = pwd_context.hash(user.password)
    create_user(user.username, user.email, hashed_password)
    return {"message": "Usuário registrado com sucesso"}

@app.post("/login")
def login(login_data: Login):
    user = get_user_by_username(login_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    stored_hash = user[2]
    if not pwd_context.verify(login_data.password, stored_hash):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    return {"message": "Login bem-sucedido"}
