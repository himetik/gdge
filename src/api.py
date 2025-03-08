from fastapi import FastAPI
from src.app import echo


app = FastAPI()


@app.get("/echo/{x}")
def get_echo(x: str):
    return {"echo": echo(x)}
