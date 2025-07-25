from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
import random
app = FastAPI()

# Modèle de citation
class Quote(BaseModel):
    author: str
    content: str

# Base de données "en mémoire"
quotes_db = [
    {"author": "Albert Einstein", "content": "La vie c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre."},
    {"author": "Confucius", "content": "Choisissez un travail que vous aimez et vous n'aurez pas à travailler un seul jour de votre vie."},
    {"author": "Oscar Wilde", "content": "Soyez vous-même, les autres sont déjà pris."}
]

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de citations !"}

@app.get("/quote")
def get_random_quote():
    return random.choice(quotes_db)

@app.get("/quotes")
def get_all_quotes():
    return quotes_db

@app.post("/quote")
def add_quote(quote: Quote):
    quotes_db.append(quote.dict())
    return {"message": "Citation ajoutée avec succès.", "quote": quote}

@app.get("/hello")
def hello():
    return "hello world"

@app.get("/welcome")
def welcome(name: str):
    return {"message": f"Welcome {name}"}

students_db = []

class StudentAttribute(BaseModel):
    reference: str
    FirstName: str
    LastName: str
    Age: int

@app.post("/students", status_code=201)
def add_students(students: list[StudentAttribute]):
    for student in students:
        students_db.append(student.dict())
    return students_db

@app.get("/students", status_code=200)
def get_students():
    return students_db

@app.put("/student")
def student_put():
    return
