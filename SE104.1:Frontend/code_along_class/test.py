import pytest
from digitcombination import number_from_list_of_digits

#number_from_list_of_digits([1,3])

def test_check_list():
   # assert isinstance(number_from_list_of_digits([1,2]), list), "Parameter must be a list"
    assert number_from_list_of_digits([1,2]) == 12

def test_check_index_is_integer():
    with pytest.raises(TypeError):
        number_from_list_of_digits([1, 'a', 4])


def test_check_if_index_is_single_digit():
    with pytest.raises(ValueError):
        number_from_list_of_digits([1, 14, 4])

def test_check_empty_list():
    assert number_from_list_of_digits([]) is None

def test_list_is_none():
    with pytest.raises(TypeError):
        number_from_list_of_digits(None)