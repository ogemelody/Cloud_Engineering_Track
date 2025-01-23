# Function - Is Divisible by
def is_divisible_by(number, by):
    if (number % by) == 0:  # checks if the reminder is 0
        return True
    else:
        return False

# Function - Is Prime?
def is_prime(number):
    if 1 < number <= 2:
        return True
    elif number > 2:
        if number // number == 1 and number // 1 == number and number % 2 != 0:
            return True
    return False

# Primes in Range
def primes_in_range(start, end):
    for number in range(start, end):
        if is_prime(number):
            print(f"The number {number} is prime")

def main():
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    number = int(input("Enter number: "))
    primes_in_range(start, end)
    is_prime(number)


if __name__ == "__main__":
    main()