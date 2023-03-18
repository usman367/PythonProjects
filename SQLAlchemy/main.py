from os import stat
from fastapi import FastAPI,status, HTTPException
from pydantic import BaseModel  # Used to create a schema class, helps us serialise every object that is returned as an object
from typing import Optional, List  # For optional parameters
import models
from database import SessionLocal

app = FastAPI()

class Item(BaseModel):  # serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode = True


db = SessionLocal()


# We use the response model to serialise the object to return ou JSON
@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    pass


@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('/items')
def create_an_item():
    pass

@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    pass



