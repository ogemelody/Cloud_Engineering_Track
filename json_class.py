import json

"""star_wars =
{
	"name": "Alderaan",
	"rotation_period": "24",
	"orbital_period": "364",
	"diameter": "12500",
	"climate": "temperate",
	"gravity": "1 standard",
	"terrain": "grasslands, mountains",
	"surface_water": "40",
	"population": "2000000000",
	"residents": [
		"https://swapi.py4e.com/api/people/5/",
		"https://swapi.py4e.com/api/people/68/",
		"https://swapi.py4e.com/api/people/81/"
	],
	"films": [
		"https://swapi.py4e.com/api/films/1/",
		"https://swapi.py4e.com/api/films/6/"
	],
	"created": "2014-12-10T11:35:48.479000Z",
	"edited": "2014-12-20T20:58:18.420000Z",
	"url": "https://swapi.py4e.com/api/planets/2/"
}

data = json.loads(star_wars)

print(f"Planet name: {data['name']}")
print(f"Climate: {data['climate']}")
print(f"Terrain: {data['terrain']}")
print(f"Appeared in films: {len(data['films'])}")
print("-------------\n")
#exercise 2

person_14 = 
    {
	"name": "Han Solo",
	"height": "180",
	"mass": "80",
	"hair_color": "brown",
	"skin_color": "fair",
	"eye_color": "brown",
	"birth_year": "29BBY",
	"gender": "male",
	"homeworld": "https://swapi.py4e.com/api/planets/22/",
	"films": [
		"https://swapi.py4e.com/api/films/1/",
		"https://swapi.py4e.com/api/films/2/",
		"https://swapi.py4e.com/api/films/3/",
		"https://swapi.py4e.com/api/films/7/"
	],
	"species": [
		"https://swapi.py4e.com/api/species/1/"
	],
	"vehicles": [],
	"starships": [
		"https://swapi.py4e.com/api/starships/10/",
		"https://swapi.py4e.com/api/starships/22/"
	],
	"created": "2014-12-10T16:49:14.582000Z",
	"edited": "2014-12-20T21:17:50.334000Z",
	"url": "https://swapi.py4e.com/api/people/14/"
}

person_14_details = json.loads(person_14)

print(f"Starship name: {person_14_details['name']}")
print(f"Crew: {person_14_details['']} ")
print(f"Consumables: {person_14_details['']} ")
print(f"Appeared in films: {len(person_14_details['films'])} ")

"""

cars_data = """
    [
   {
      "name": "Jonathan",
      "grades": [100, 98, 33, 55]
   },
   {
      "name": "Rona",
      "grades": [99, 22]
   },
   {
      "name": "Valentin",
      "grades": [99, 99, 98, 97, 95]
   }
]
""""""
# Load JSON data from the file
#with open("cars.json", "r") as file:
data = json.loads(cars_data)  # Read JSON correctly
print(data)
"""

