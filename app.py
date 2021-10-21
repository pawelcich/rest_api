import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


class Item(BaseModel):
    item_1: int
    item_2: int


class Operation(str, Enum):
    add = 'add'
    subtract = 'subtract'
    multiply = 'multiply'
    divide = 'divide'


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to basic math operations api !"}


@app.post("/{operation}", tags=['Basic math operations'])
async def operate(operation: Operation, item: Item):
    if operation.value == 'add':
        return {"result": item.item_1 + item.item_2}
    if operation.value == 'subtract':
        return {"result": item.item_1 - item.item_2}
    if operation.value == 'multiply':
        return {"result": item.item_1 * item.item_2}
    if operation.value == 'divide':
        return {"result": item.item_1 / item.item_2}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
