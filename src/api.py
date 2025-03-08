from src.app import app
from src.utils import echo


@app.get("/echo/{x}")
def get_echo(x: str):
    return {"echo": echo(x)}
