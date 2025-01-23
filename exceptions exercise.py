# 1
'''
def is_divisible_by(number, divisor):
    if isinstance(number, int):
            if type(divisor) is int:
                return number % divisor == 0

    else:
        return  "Type Error"

try:
    print(is_divisible_by(10, 2))
    print(is_divisible_by(10, "2"))
except TypeError as e:
    print(e)
finally:
    print("code runs successfully")



#2 using IF conditional
def add_percentage(price, percentage):
    if isinstance(price,(int,float)):
        if type(percentage) == int or type(percentage) == float:
            print(price,percentage)
            return price + (percentage * price)
        else:
            print ("The percentage should be int or float")
    print ("The price should be int or float")

add_percentage(100, 0.1)
add_percentage(100, "0.05") # Causes an exception
'''
# or
'''
def add_percentage(price, percentage):
    try:
        return price + (percentage * price)
    except TypeError as e:
        print ("Both values must be int or float")
        print(e)
    finally:
        print("Attempted to add percentage to price")
add_percentage(100, 0.1)
add_percentage(100, "0.05") # Causes an exception
'''

# 3
'''def get_grade(database, student_name):
    return database[student_name]

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

name = "John"
print(get_grade(db, name)) # all good
'''
name = "Johnn"
db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

print(get_grade(db, name))  # causes an exception


def get_grade(database, student_name):
    """

    :param database:
    :param student_name:
    :return:
    """
    input_student_name = student_name.lower()
    suggested_student_name = {}
    for key, value in database.items():
        if input_student_name in key.lower():
            suggested_student_name[key] = value
