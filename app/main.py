from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas 
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")

#Start page to know that the server is alive
@app.get("/")
def read_root():
    return{"message": "Välkommen till Todo-backend:)"}

#Get all todos from the database
@app.get("/todos", response_model=list[schemas.TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.TodoModel).all()


@app.post("/todos", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.TodoModel(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


