def factorial(n):
    """
    Calculate the factorial of a given number n.
    
    Args:
    - n: An integer
    
    Returns:
    - The factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
    - n: An integer
    
    Returns:
    - The nth Fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm.
    
    Args:
    - arr: A list of integers
    
    Returns:
    - The sorted array
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def divide(a, b):
    """
    Divide two numbers a and b.
    
    Args:
    - a: An integer (numerator)
    - b: An integer (denominator)
    
    Returns:
    - The result of a divided by b
    """
    return a / b

def main():
    # Calculate factorial
    print("Factorial of 5:", factorial(5))
    
    # Calculate Fibonacci sequence
    print("Fibonacci sequence up to 10:", [fibonacci(i) for i in range(10)])
    
    # Sort an array
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Sorted array:", bubble_sort(arr))
    
    # Divide two numbers
    print("Result of dividing 10 by 3:", divide(10, 3))

if __name__ == "__main__":
    main()
