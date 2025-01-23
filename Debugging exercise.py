'''
def is_odd_number(num):
  """ Checks if num is odd """
  if num % 2 == 0:
    return False
  else:
    return True

def main():
	print(is_odd_number(4)) # Expected False
	print(is_odd_number(7)) # Expected True

if __name__ == "__main__":
	main()

'''

#2#
'''
def get_inputs():
    """ Get user inputs """
    result = []
    for i in range(3):
        val = int(input("Enter a number: "))
        while True:
            try:
                result.append(val)
                break
            except Exception as e:
                print(e)
    return result

def sum_of_even(numbers):
    """ Sum up all the even numbers in the list """

    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

def main():
    numbers = get_inputs()
    result = sum_of_even(numbers)
    print(f"To sum of even: {result}")


if __name__ == "__main__":
    main()

'''
##3
def remove_special_char(username):
    """ Remove special characters and space from the username """
    updated_username = ""
    for char in username:
        if  not char in  ";.@#$%ˆ&*:_ ":
            updated_username += char
    return updated_username

def add_at_symbol(username):
    """ add the @ symbol at the end of the username """
    return username + "@"

def add_domain_name(username):
    """ add the domain (mail.com) name to the username """
    return "mail" + username + ".com"

def main():
    username = "user&#123_ @" # username we want to convert to email
    new_username = remove_special_char(username)
    new_username_with_at = add_at_symbol(new_username)
    user_email = add_domain_name(new_username_with_at)
    print(user_email) # Expected user123@mail.com

if __name__ == "__main__":
    main()