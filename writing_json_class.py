import json

#to read a json file
with open( "movies.json", "r") as json_file:
    data = json.load(json_file) #save file into data object

new_movie = {
    "id": 5,
    "title": "Mother",
    "year": 2024,
    "genre": ["Sci-Fi", "Drama"],
    "rating": 1
}

data["movies"].append(new_movie)

with open("movies.json", "w") as json_file:
    json.dump(data, json_file, indent= 4)

print(data)

