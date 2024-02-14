def find_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test the function
numbers = [5, 7, 9, 3, 1]
average = find_average(numbers)
print("The average is:", average)
