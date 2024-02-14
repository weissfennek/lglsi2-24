def check_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test with a prime number
print("Is 11 a prime number?", check_prime(11))

# Test with a non-prime number
print("Is 10 a prime number?", check_prime(10))

# Test with a negative number
print("Is -5 a prime number?", check_prime(-5))
