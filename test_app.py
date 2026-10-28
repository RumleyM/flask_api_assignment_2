import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/hello?name=Matiwos")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Matiwos!"}


def test_hello_default(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_sum(client):
    response = client.post("/sum", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"sum": 6}


def test_sum_bad_request(client):
    response = client.post("/sum", json={})
    assert response.status_code == 400