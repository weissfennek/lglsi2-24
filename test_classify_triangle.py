def classify_triangle(side1, side2, side3):
    if side1 == side2 or side1 == side3 or side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        print("Scalene")

def test_classify_triangle():
    assert classify_triangle(0,0,0)=="les cote ne doivent pas etre 0"
    assert classify_triangle(1,1,10)=="la somme de deux cote doit etre > au troisieme "
    assert classify_triangle(4,4,4)=="Equilaterale"
    assert classify_triangle(4, 4,3) == "Isocele"
    assert classify_triangle(5, 4, 3) =="Scalene"
