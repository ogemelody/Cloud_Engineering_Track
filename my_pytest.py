import pytest
import unit_testing
def test_sanity():
    result = unit_testing.find_min_max([2,3,6,7])
    assert result == (2,7)

def test_emptylist():
    result = unit_testing.find_min_max([])
    #assert result == None , "Number list should not be empty"
    assert result == False