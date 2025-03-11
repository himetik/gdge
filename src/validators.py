from fastapi import HTTPException
from src.config import ECHO_MAX_LENGTH


def validate_endpoint_input(x):
    if len(x) > ECHO_MAX_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input too long. Max length is {ECHO_MAX_LENGTH} characters."
        )
    return x
