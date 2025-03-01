import json

def load_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

def attribute(data_file):
    animals = data_file
   # print(animals[0])
    for animal in animals:
        name = animal['name']
        diet = animal['characteristics']['diet']
        location = animal['locations'][0]
       # type = animal.get('characteristics', {}).get('type', None)
        type_value = animal['characteristics'].get('type')
        if type_value:
            print(f"Name: {name}\nDiet:{diet}\nLocation: {location}\n Type: {type_value}\n ")
        print(f"Name: {name}\nDiet:{diet}\nLocation: {location}\n")


def main():
    file_path = "animal_data.json"
    data_file = load_data(file_path)
    attribute(data_file)



if __name__ == "__main__":
    main()
