from typing import List
from pydantic import BaseModel, Field


class People(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    home_world: str = Field(alias="homeworld")
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    created: str
    edited: str
    url: str
