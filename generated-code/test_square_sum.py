import pytest

from square_sum import calculate_square_sum

def test_calculate_square_sum():
    # Test with a list of integers
    numbers = [1, 2, 3, 4, 5]
    assert calculate_square_sum(numbers) == 55 

    # Test with an empty list
    assert calculate_square_sum([]) == 0  # The sum of squares of an empty list should be 0

    # Test with a list containing negative numbers
    numbers = [-1, -2, -3, -4, -5]
    assert calculate_square_sum(numbers) == 55  # Same result as the list of positive numbers, as squaring the negative numbers yields positive results

    # Test with a list containing float numbers
    numbers = [1.5, 2.5, 3.5]
    assert calculate_square_sum(numbers) == 20.75  # Expected result is the sum of squares: 1.5^2 + 2.5^2 + 3.5^2 = 18.75

    #Test with a list containing float and integer numbers
    numbers=[1.5,3,8,9]
    assert calculate_square_sum(numbers) == 156.25