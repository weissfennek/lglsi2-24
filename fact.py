def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = input("Enter a number: ")
print("Factorial of " + number + " is: " + factorial(number))
