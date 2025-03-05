def is_sum_of_two_primes(number):
    try:
        if number % 2 == 1:  # Sum of two primes will usually be even, so we check for odd numbers
            return False
        for i in range(2, number):
            good = True
            # Check if i is a prime
            x = 2
            while x < i:
                if i % x == 0:
                    good = False
                    break
                x += 1
            if good:
                # i is a prime, now check if j = number - i is prime
                j = number - i
                if j >= 2:  # j must be greater than or equal to 2 to be prime
                    good2 = True
                    x = 2
                    while x < j:
                        if j % x == 0:
                            good2 = False
                            break
                        x += 1
                    if good2:
                        print(f"The number {number} equals the sum of {i} and {j}")
                        return True  # Return True once a valid pair is found
        return False  # Return False if no valid pair is found
    except TypeError:
        print("Invalid type entered, please provide an integer.")
        return False


# Input from user
try:
    number = int(input("Enter a number: "))  # Ensure that the input is an integer
    print(is_sum_of_two_primes(number))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
