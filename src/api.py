from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from src.app import app
from src.utils import echo, get_flag_by_country
from src.config import MAX_LENGTH
from src.instead_of_db import countries


@app.get("/")
def get_docs():
    return RedirectResponse(url="/docs")


@app.get("/echo/{x}")
def get_echo(x: str):
    if len(x) > MAX_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input too long. Max length is {MAX_LENGTH} characters."
        )
    return {"echo": echo(x)}


@app.get("/echo/")
def get_echo_without_data():
    raise HTTPException(
        status_code=400,
        detail="Missing required parameter 'x' in the URL path. Use /echo/{x}."
    )


@app.get("/country_flag/{country}")
def get_country_flag(country):
    flag = get_flag_by_country(countries, country)
    return {"country flag": flag}


@app.get("/country_flag/")
def get_country_flag_without_data():
    raise HTTPException(
        status_code=400,
        detail="Missing required parameter 'country_flag' in the URL path. Use /echo/{country_flag}."
    )
