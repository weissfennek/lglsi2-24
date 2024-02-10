# -*- encoding:utf-8 -*-

def calculate_square_sum(numbers: list) -> int | float:
    """
    Calculate the sum of squares for a given list of numbers.
    """
    squared_numbers = [num ** 2 for num in numbers]
    return sum(numbers)

# List of integer
mixed_numbers = [1, 2, "3", 4, 5]

# Function call with the mixed_numbers list
result = calculate_square_sum(mixed_numbers)


# Display result
print(f"The sum of squares is: {result}")
