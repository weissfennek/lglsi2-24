import pytest
def is_prime(n):                                
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(n) :
    print(" ce nombre est   premier")
else:
    print("ce nombre n'est pas  premier") 

def test_is_prime():
    assert is_prime(4)==False