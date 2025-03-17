from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []

class Task(BaseModel):
    task: str
    priority: int

@app.post('/task')
def create_task(task: Task):
    tasks.append(task)
    return {'message': 'Criado com sucesso!', 'task': task}
