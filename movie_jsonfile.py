import json

with open('movies.json', 'r') as json_file:
    # Load the data from the JSON file
    data = json.load(json_file)
print(data)
new_movie = {
    "id": 4,
    "title": "Mother",
    "year": 2025,
    "genre": ["Sci-Fi", "Drama"],
    "rating": 10
}

#add data(new_movie)
data["movies"].append(new_movie)


with open('movies.json', 'w') as json_file:
    # Load the data from the JSON file
    json.dump(data,json_file, indent =4)

print("Movie added successfully!")
#print(data)
