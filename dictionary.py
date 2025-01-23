#Class

#dictionary
example = {
    'basket': ['apple', 'orange'],
    'price': 45,
    'paid': False,
    1: True
}
'''
#constructor dict()
examples2 = dict(
    basket = ['apple', 'orange'],
    price = 45,
    paid = False

)
print(examples2['basket'])

#using get
print(example.get('price'))

if example.get('price') == None:
    print('we dont price yet')
    example['prices'] = [23,45,56]

print(example)

#working with duplicate keys, it overwrite existing one
duplicate_keys = {
    "Key_1" : 23,
    "Key_1" : 'Egg'
}

print(duplicate_keys.get('Key_1')) # overwrite the first
'''
#Methods
#adding  an element
example["name"] = "Melody"
print(example)

#removing an element
del example["name"] #using del
print(example)
example.pop('basket') # using pop
print(example)


# modify
example['paid'] = True
print(example)


student = {}
student['name '] = "mARIA"
student

#iterating
for value in example.values():
    print(value)


#diction of dictionary -nested Dictionary
dogs = {

     "dog_001": {

         "name": "Buddy",

         "breed": "Golden Retriever",

         "age": 5,

         "owner": {

             "name": "Alice Johnson",

         },

     },

     "dog_002": {

         "name": "Max",

         "breed": "Beagle",

         "age": 3,

         "owner": {

             "name": "Bob Smith",

         },

     },

     "dog_003": {

         "name": "Bella",

         "breed": "German Shepherd",

         "age": 4,

         "owner": {

             "name": "Charlie Davis",

         },

     }

  }

#to get KEYS
for key in dogs.keys():
    print(key)

#if you dont specify you only get keys
for key in dogs:
    print(key)

#for value yo uneed to specify .values()
for value in dogs.values():
    print(value)


#ITEMS: to get key and value
for key in dogs.items():
    print(key)

#to get keys just from dog-001
for key in dogs['dog_001']:
    print(key)

#value of dog_001
for value in dogs['dog_001'].values():
    print(value)

#to get items
for value in dogs['dog_001'].items():
    print(value)


#retrieve the owner of specific dog - going into a nested dictionary
owner_dog_1 = dogs['dog_001']['owner']['name']
print(owner_dog_1)


'''
#Exercise
vehicle = {
    'brand': 'Audi',
    'Model': 'Q3',
    'year': 2012
}
print(vehicle)

vehicle['color'] = 'blue'

print(vehicle)

#change year to current
vehicle['year'] = 2025
print(vehicle)

#print out all the keys and values, full dictionary

print('keys', vehicle.keys())
print('values', vehicle.values())
print("full", )
'''

#Classwork
student = {
    'John': 6,
    'Melody': 8
}
#add new student
student['James'] = 23
print(student)

#remove a student
del student['John']
print(student)

#change the seat number
student['James'] = 12
print(student)

#Check if a specific student is in the dictionary
if student.get("John") == None:
    print('not in the class')


#Print all the students' names. Each printed line should be 1 student.

for name in student:
    print(name)


#Task 2
library_inventory = {
    "978-0143128540": {"title": "Sapiens", "author": "Yuval Noah Harari", "year_published": 2015},
    "978-0307277671": {"title": "The Road", "author": "Cormac McCarthy", "year_published": 2006}
}

#Create a dictionary using the book’s ISBN as the key and a dictionary as the value
library_inventory["234"]