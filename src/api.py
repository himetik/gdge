from fastapi import HTTPException
from src.app import app
from src.utils import echo
from src.config import MAX_LENGTH


@app.get("/echo/{x}")
def get_echo(x: str):
    if len(x) > MAX_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input too long. Max length is {MAX_LENGTH} characters."
        )
    return {"echo": echo(x)}


@app.get("/echo/")
def get_echo_missing():
    raise HTTPException(
        status_code=400,
        detail="Missing required parameter 'x' in the URL path. Use /echo/{x}."
    )
