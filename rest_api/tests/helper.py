from rest_api.models.people import People
from rest_api.models.planets import Planets
from rest_api.models.starships import Starships


def create_people_model():
    return People(
        name="Luke Skywalker",
        height="172",
        mass="77",
        hair_color="blond",
        skin_color="fair",
        eye_color="blue",
        birth_year="19BBY",
        gender="male",
        homeworld="https://swapi.dev/api/planets/1/",
        films=[
            "https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/", "https://swapi.dev/api/films/6/"
        ],
        species=[],
        vehicles=["https://swapi.dev/api/vehicles/14/", "https://swapi.dev/api/vehicles/30/"],
        starships=["https://swapi.dev/api/starships/12/", "https://swapi.dev/api/starships/22/"],
        created="2014-12-09T13:50:51.644000Z",
        edited="2014-12-20T21:17:56.891000Z",
        url="https://swapi.dev/api/people/1/"
    )


def create_planets_model():
    return Planets(
        name="Yavin IV",
        rotation_period="24",
        orbital_period="4818",
        diameter="10200",
        climate="temperate, tropical",
        gravity="1 standard",
        terrain="jungle, rainforests",
        surface_water="8",
        population="1000",
        residents=[],
        films=[
            "https://swapi.dev/api/films/1/"
        ],
        created="2014-12-10T11:37:19.144000Z",
        edited="2014-12-20T20:58:18.421000Z",
        url="https://swapi.dev/api/planets/3/"
    )


def create_starships_model():
    return Starships(
        name="Death Star",
        model="DS-1 Orbital Battle Station",
        manufacturer="Imperial Department of Military Research, Sienar Fleet Systems",
        cost_in_credits="1000000000000",
        length="120000",
        max_atmosphering_speed="n/a",
        crew="342,953",
        passengers="843,342",
        cargo_capacity="1000000000000",
        consumables="3 years",
        hyperdrive_rating="4.0",
        MGLT="10",
        starship_class="Deep Space Mobile Battlestation",
        pilots=[],
        films=[
            "https://swapi.dev/api/films/1/"
        ],
        created="2014-12-10T16:36:50.509000Z",
        edited="2014-12-20T21:26:24.783000Z",
        url="https://swapi.dev/api/starships/9/"
    )