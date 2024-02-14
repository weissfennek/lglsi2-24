def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))  # Convert input to integer
result = factorial(number)
print("Factorial of", number, "is:", result)  # Print the result separately
