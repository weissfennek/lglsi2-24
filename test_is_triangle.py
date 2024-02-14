def is_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    if side1 >= side2 - side3 or side2 >= side1 + side3 or side3 > side1 + side2:
        return True

    return False
def test_is_triangle():
    assert is_triangle(0,2,3)==False
    assert is_triangle(5, 2, 3) == False
    assert is_triangle(10, 5, 4) == True
