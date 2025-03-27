# main.py - FastAPI application
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import engine, Base, SessionLocal
from models import Item, ItemCreate
from dependencies import get_db

app = FastAPI()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    item = Item(name=item.name, nested=item.nested)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
