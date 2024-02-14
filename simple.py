import pytest

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_prime(n):
    if is_prime(n):
        return f"{n} est premier"
    else:
        return f"{n} n'est pas premier"

# Example usage
n = 7
print(check_prime(n))

# Pytest test case
def test_is_prime():
    assert is_prime(4) == False
    # Add more test cases as needed

# Run the tests with Pytest
if __name__ == "__main__":
    pytest.main()
