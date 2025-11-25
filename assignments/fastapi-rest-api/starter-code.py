# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API!"}

# Add more endpoints for CRUD operations below
