import pytest
from MoomenCode import classify_triangle, is_triangle, analyze_triangle

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

def test_analyze_triangle():
    assert analyze_triangle(3, 3, 3) == "The triangle is: Equilateral"
    assert analyze_triangle(3, 3, 4) == "The triangle is: Isosceles"
    assert analyze_triangle(3, 4, 5) == "The triangle is: Scalene"
    assert analyze_triangle(1, 1, 3) == "No, the dimensions do not form a triangle."

