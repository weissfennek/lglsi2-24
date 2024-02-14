def find_average(numbers):
    if not numbers:
        print("La liste est vide.")
        return None

    if not all((type(num) == int or type(num) == float) for num in numbers):
        print("La liste contient des éléments non numériques.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Test the function
numbers = [5, 7, 9, 3, 1]
average = find_average(numbers)
print("The average is:", average)