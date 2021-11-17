import uvicorn
from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to basic math operations api!"}


@app.get("/add")
async def add(a: int, b: int):
    return {"result": a + b}


@app.get("/subtract")
async def subtract(a: int, b: int):
    return {"result": a - b}


@app.get("/multiply")
async def multiply(a: int, b: int):
    return {"result": a * b}


@app.get("/divide")
async def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(
            status_code=404, detail='Division by 0 not allowed!')
    return {"result": a / b}


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
