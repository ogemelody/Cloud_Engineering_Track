# Function - Is Divisible by
def is_divisible_by(number, by):
    return (number % by) == 0  # checks if the reminder is 0


# Function - Is Prime?
def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if is_divisible_by(number, x):
            return False
    return True


# Primes in Range
def primes_in_range(start, end):
    for number in range(start, end):
        if is_prime(number):
            print(f"The number {number} is prime")


# main
def main():
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    primes_in_range(start, end)
    print(is_divisible_by(10, 2))


if __name__ == "__main__":
    main()
