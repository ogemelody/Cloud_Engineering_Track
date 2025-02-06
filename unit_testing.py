# Class
"""def count_character(string,char):
    if not char:
        return None
    count = 0
    for c in string.lower():
        if c == char:
            count += 1
    return count

#assert <condition>, message
assert count_character('colorado', 'o') == 3, \
    "No finding the right number of o's in colorado"

if count_character("colorado", 'o')== 3:
        print("Test Passed: right amount")

else:
    print("Test failed: if No finding the right number of o's in colorado")

print(count_character('colorado', 'o'))

"""
from numpy.matlib import empty


# Exercise
def find_min_max(nums):
    """
    Returns a tuple containing the minimum and maximum numbers from the input list.

    Parameters:
    nums (list): A list of numbers.

    Returns:
    tuple: A tuple containing the minimum and maximum numbers.

    If the list is empty return None.

    If the parameter is wrong datatype, or list has non-numeric elementsreturn False.
    """
    if not isinstance(nums, list):
        return None
    if not nums :
        return False
    # Initialize min and max variables with the first element of the list
    minimum = nums[0]
    maximum = nums[0]

    # Iterate through the list to find the minimum and maximum numbers
    for num in nums[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum, maximum

assert find_min_max([]) == None, "List can not be empty"

print("Test passed: Empty list returns None")

print(find_min_max([]))


