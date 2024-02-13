import pytest
from Test_moomenCode import classify_triangle, is_triangle

def test_classify_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_classify_isosceles_triangle():
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(4, 3, 3) == "Isosceles"
    assert classify_triangle(3, 4, 3) == "Isosceles"

def test_classify_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene"

def test_is_triangle_valid():
    assert is_triangle(3, 4, 5) == True
    assert is_triangle(5, 12, 13) == True

def test_is_triangle_invalid():
    assert is_triangle(1, 1, 3) == False
    assert is_triangle(0, 0, 0) == False
    assert is_triangle(-1, -1, -1) == False

if __name__ == "__main__":
    pytest.main()

