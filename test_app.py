from typing import Text
from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to basic math operations api !"}


def test_add():
    response = client.get("/add?a=12&b=2")
    assert response.status_code == 200
    assert response.json() == {
        "result": 14
    }


def test_subtract():
    response = client.get("/subtract?a=12&b=2")
    assert response.status_code == 200
    assert response.json() == {
        "result": 10
    }


def test_string():
    response = client.get("/add?a=tt&b=2")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': [
        'query', 'a'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]}


def test_multiply():
    response = client.get("/multiply?a=12&b=2")
    assert response.status_code == 200
    assert response.json() == {
        "result": 24
    }


def test_divide():
    response = client.get("/divide?a=12&b=2")
    assert response.status_code == 200
    assert response.json() == {
        "result": 6
    }


def test_divide_by_0():
    response = client.get("/divide?a=12&b=0")
    assert response.status_code == 404
    assert response.json() == {"detail": 'Division by 0 not allowed!'}
