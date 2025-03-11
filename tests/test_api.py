import requests
from src.config import ECHO_MAX_LENGTH


def test_get_docs():
    url = "http://localhost:5000/"
    response = requests.get(url)
    assert response.status_code == 200
    assert '<div id="swagger-ui">' in response.text
    assert "Swagger UI" in response.text


def test_get_echo():
    url = "http://localhost:5000/echo/test"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {
        "echo": "test"
    }


def test_get_echo_exceeded_length():
    url = f'http://localhost:5000/echo/{"a" * (ECHO_MAX_LENGTH + 1)}'
    response = requests.get(url)
    assert response.json() == {
        "detail": "Input too long. Max length is 80 characters."
    }


def test_get_echo_without_data():
    url = "http://localhost:5000/echo/"
    response = requests.get(url)
    assert response.json() == {
        "detail": "Missing required parameter 'x' in the URL path. Use /echo/{x}."
    }


def test_get_country_flag():
    url = "http://localhost:5000/country_flag/rwanda"
    response = requests.get(url)
    assert response.json() == {
        "country flag": "🇷🇼"
    }


def test_get_country_flag_without_data():
    url = "http://localhost:5000/country_flag/"
    response = requests.get(url)
    assert response.json() == {
        "detail": "Missing required parameter 'country_flag' in the URL path. Use /echo/{country_flag}."
    }


def test_get_country_flag_nonexistent_country():
    url = "http://localhost:5000/country_flag/winterfell"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json() == {
        "detail": "The country not found",
    }
