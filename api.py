from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello/{name}")
def read_item(name: str, age: Optional[int] = None):
    return {"hello": f"hello {name}", "age": f"la edad de la persona es {age}"}
