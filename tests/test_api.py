import requests
from src.config import MAX_LENGTH


def test_get_echo():
    url = "http://localhost:5000/echo/test"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {
        "echo": "test"
    }


def test_get_echo_exceeded_length():
    url = f'http://localhost:5000/echo/{"a" * (MAX_LENGTH + 1)}'
    response = requests.get(url)
    assert response.json() == {
        "detail": "Input too long. Max length is 80 characters."
    }


def test_get_echo_without_parameter():
    url = "http://localhost:5000/echo/"
    response = requests.get(url)
    assert response.json() == {
        "detail": "Missing required parameter 'x' in the URL path. Use /echo/{x}."
    }
