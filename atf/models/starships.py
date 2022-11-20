from typing import List
from pydantic import BaseModel, Field


class Starships(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    mglt: str = Field(alias="MGLT")
    starship_class: str
    pilots: List[str]
    films: List[str]
    created: str
    edited: str
    url: str
