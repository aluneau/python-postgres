# models.py - Define database models
from db import Base  # Import Base from db.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from pydantic import BaseModel

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    nested = Column(JSONB)

class ItemCreate(BaseModel):
    name: str
    nested: dict