from fastapi.testclient import TestClient

from rest_api.main import app
from rest_api.models.people import People
from rest_api.models.planets import Planets
from rest_api.models.starships import Starships

client = TestClient(app)


def test_get_people_existing_record():
    response = client.get("/api/people/0")
    assert response.status_code == 200
    response_json = response.json()
    assert People.parse_obj(response_json)


def test_get_people_non_existing_record():
    response = client.get("/api/people/1000")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == "Person not found"


def test_get_planets_existing_record():
    response = client.get("/api/planets/0")
    assert response.status_code == 200
    response_json = response.json()
    assert Planets.parse_obj(response_json)


def test_get_planets_non_existing_record():
    response = client.get("/api/planets/1000")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == "Planet not found"


def test_get_spaceships_existing_record():
    response = client.get("/api/starships/0")
    assert response.status_code == 200
    response_json = response.json()
    assert Starships.parse_obj(response_json)


def test_get_spaceships_non_existing_record():
    response = client.get("/api/starships/1000")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == "Starship not found"


