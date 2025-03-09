import requests


def test_get_echo():
    response = requests.get("http://localhost:5000/echo/test")
    assert response.status_code == 200
    assert response.json() == {"echo": "test"}
