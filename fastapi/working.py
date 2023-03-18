from fastapi import FastAPI, Path, Query  # Importing the FastAPI class/module form fastapi
from typing import Optional # For making stuff optional
from pydantic import BaseModel # For request body

app = FastAPI()  # Creates an API object, initialises our API

# For the request body
class Item(BaseModel):  # Inherits from BaseModel
    name: str
    price: float
    brand: Optional[str] = None # Made the brand optional

class UpdateItem(BaseModel):  # Inherits from BaseModel
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None # Made the brand optional


# Setting up an endpoint:
# An endpoint is the point of entry in a communication channel
# when two systems are interacting
# E.g., /hello or /get-item
# Get returns information, POST creates something
# PUT updates something
# DELETE deletes something
@app.get("/")  # Defining the route/ endpoint
def home():
    return {"Data: Testing"}  # Returning some kind of data, it will automatically be converted into JSON

# To run it: cd C:\Users\usman\PycharmProjects\fastapi
# uvicorn working:app --reload
# working is the name of this file and :app is the object we created above that we want to run
# Works on: http://127.0.0.1:8000/


@app.get("/about")
def about():
    return {"Data: About"}
# Works on http://127.0.0.1:8000/about


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


inventory = {}

# Setting up an endpoint that can retrieve item information based on its ID
@app.get("/get-item/{item_id}")  # We want the user to be able yo pass an ID for the item
# Path allows you to add more details/constraints (using gt (greater than), lt, le, ge) on our actual parameter
def get_item(item_id: int = Path(None, description="The ID of the Item you'd like to view", gt=0)):  # We take in a parameter, and we tell fast api this is supposed to be an integer, otherwise it will automatically return an error message
    return inventory[item_id]

# Query parameter e.g. ?someVariableName=/tim&msg=fail"
@app.get("/get-by-name")
def get_item(name: str): # = None would make the parameter name optional
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data: Not found"}
# This will now work: http://127.0.0.1:8000/get-by-name?name=Milk


# Request body - for sending information into databases
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory: # If the id is already in inventory, return an error
        return {"Error": "Item ID already exists."}

    # Otherwise, adds this data to inventory
    inventory[item_id] = item
    return inventory[item_id]



# Updating an item
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory: # If the item is not in inventory, return an error
        return {"Error": "Item does not exist."}

    # Otherwise, override the item with the new item
    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


# Deleting an item
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of item to delete", gt=0)):
    if item_id not in inventory:
        return {"Error: ID does not exist"}

    del inventory[item_id]
    return {"Success: Item deleted!"}








