# test_calculer_moyenne.py

from moyenne import calculer_moyenne

def test_calculer_moyenne_liste_vide():
    assert calculer_moyenne([]) == 0

def test_calculer_moyenne_entiers():
    notes = [85, 90, 78, 92]
    assert calculer_moyenne(notes) == 86.25

def test_calculer_moyenne_floats():
    notes = [85.5, 90.5, 78.5, 92.5]
    assert calculer_moyenne(notes) == 86.75

def test_calculer_moyenne_melange_entiers_floats():
    notes = [85, 90.5, 78, 92.5]
    assert calculer_moyenne(notes) == 86.5

def test_calculer_moyenne_notes_negatives():
    notes = [-85, -90, -78, -92]
    assert calculer_moyenne(notes) == -86.25

def test_calculer_moyenne_notes_melangees():
    notes = [85, "a", 78, 92]
    assert calculer_moyenne(notes) is None
