from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_404_NOT_FOUND

from rest_api.data_generator import PeopleDataGenerator, PlanetsDataGenerator, StarshipsDataGenerator
from rest_api.helper import get_api_data
from rest_api.models.error_msg import ErrorMsg
from rest_api.models.people import People
from rest_api.models.planets import Planets
from rest_api.models.starships import Starships

app = FastAPI()
people_data = get_api_data(PeopleDataGenerator(Path.joinpath(Path(__file__).resolve().parent,
                                                             "sample_data", "people.json")))
planets_data = get_api_data(PlanetsDataGenerator(Path.joinpath(Path(__file__).resolve().parent,
                                                               "sample_data", "planets.json")))
starships_data = get_api_data(StarshipsDataGenerator(Path.joinpath(Path(__file__).resolve().parent,
                                                                   "sample_data", "starships.json")))


@app.get("/api/people/{person_id}", response_model=People,
         responses={HTTP_404_NOT_FOUND: {"content": {"application/json": {"example": {"detail": "Person not found"}}},
                                         "model": ErrorMsg}})
def get_people(person_id: int) -> BaseModel:
    """
    Returns person with matching person_id if person with provided id doesn't exist return 404
    """
    if person_id not in people_data:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Person not found")
    return people_data[person_id]


@app.get("/api/planets/{planet_id}", response_model=Planets,
         responses={HTTP_404_NOT_FOUND: {"content": {"application/json": {"example": {"detail": "Planet not found"}}},
                                         "model": ErrorMsg}})
def get_planets(planet_id: int) -> BaseModel:
    """
    Returns planet with matching planet_id if planet with provided id doesn't exist return 404
    """
    if planet_id not in planets_data:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Planet not found")
    return planets_data[planet_id]


@app.get("/api/starships/{starship_id}", response_model=Starships, responses={
    HTTP_404_NOT_FOUND: {"content": {"application/json": {"example": {"detail": "Starship not found"}}},
                         "model": ErrorMsg}})
def get_starships(starship_id: int) -> BaseModel:
    """
    Returns starship with matching starship_id if starship with provided id doesn't exist return 404
    """
    if starship_id not in starships_data:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Starship not found")
    return starships_data[starship_id]
