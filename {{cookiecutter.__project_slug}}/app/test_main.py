from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_read_{{ cookiecutter.__project_slug }}():
    response = client.get("/{{ cookiecutter.__project_slug }}")
    assert response.status_code == 200

def test_read_random_{{ cookiecutter.__project_slug }}():
    response = client.get("/{{ cookiecutter.__project_slug }}/random")
    assert response.status_code == 200
    assert len(response.json()) == 5

def test_read_3_random_{{ cookiecutter.__project_slug }}():
    response = client.get("/{{ cookiecutter.__project_slug }}/random/3")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_read_bad_random_{{ cookiecutter.__project_slug }}():
    response = client.get("/{{ cookiecutter.__project_slug }}/random/string")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

