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

movies = []

class Movie(BaseModel):
    title: str
    description: str
    genre: str
    release: int
    image: str

@app.post('/movie')
def create_movie(movie: Movie):
    movies.append(movie)
    return {'message': 'Criado com sucesso!', 'movie': movie}

@app.get("/movies")
def get_movies():
    return movies
