def calculate(text_input):
    for operator in "+-*/~":  # get the operator from the user input
        # gets the first_value set of value and second set of value using the operator as a split
        if operator in text_input:
            extract_value = text_input.split(operator)
            first_value = int(extract_value[0])
            second_value = int(extract_value[1])
            print(first_value, second_value)

            if operator == "+":
                addition = first_value + second_value
                return (addition)  # addition
            elif operator == "*":
                multiplication = first_value * second_value
                return multiplication  # multiplication
            elif operator == "/":
                division = first_value / second_value
                return division  # division
            elif operator == "-":
                subtraction = first_value - second_value
                return subtraction  # subtraction
            elif operator == "~":  # Integer Division & Remainder
                division_tilde = first_value // second_value
                remainder = first_value % second_value
                return (f"{division_tilde}, \nThe remainder is, {remainder}")


print("Welcome to the Python calculator!")
num_calculation = int(input("How many calculations do you want to do?"))
for i in range(num_calculation):  #
    user_input = input("What do you want to calculate? ")
    result = calculate(user_input)
    print(f"The answer is {result}")