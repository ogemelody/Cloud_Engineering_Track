def number_from_list_of_digits(list_of_digits):
    """
    This function gets a list of int digits, like [1, 4, 0]
    And returns the number made out of the digits, as int (140).
		If there is a problem with input values, raises a ValueError.
		If there is a problem with input types, raises a TypeError.
    """
    # Ensure input is not None
    if list_of_digits is None:
        raise TypeError("Input must be a list of digits, not None.")

    # Ensure input is a list
    if not isinstance(list_of_digits, list):
        raise TypeError(f"Expected a list of digits, but got {type(list_of_digits).__name__}.")

    # Ensure all elements are integers
    if not all(isinstance(each_digit, int) for each_digit in list_of_digits):
        invalid_elements = [repr(d) for d in list_of_digits if not isinstance(d, int)]
        raise TypeError(f"All elements in the list must be integers. Invalid elements: {', '.join(invalid_elements)}.")

    # Ensure all elements are between 0 and 9
    if not all(0 <= each_digit <= 9 for each_digit in list_of_digits):
        invalid_elements = [repr(d) for d in list_of_digits if not (0 <= d <= 9)]
        raise ValueError(
            f"All elements must be single-digit integers (0-9). Invalid elements: {', '.join(invalid_elements)}.")

    # Handle an empty list (returning None instead of breaking)
    if not list_of_digits:
        return None

    return int("".join(map(str, list_of_digits)))


def main():
    try:
        # Test case with invalid input
        digit_list = ["p", 4, 0]
        print(number_from_list_of_digits(digit_list))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        # Test case with valid input
        digit_list = [1, 4, 0]
        print(number_from_list_of_digits(digit_list))  # Expected output: 140
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        # Test case with valid input
        digit_list = [11, 4, 0]
        print(number_from_list_of_digits(digit_list))  # Expected output: 140
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        # Test case with an empty list
        digit_list = []
        print(number_from_list_of_digits(digit_list))  # Expected output: 0
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        # Test case with None input
        digit_list = None
        print(number_from_list_of_digits(digit_list))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()