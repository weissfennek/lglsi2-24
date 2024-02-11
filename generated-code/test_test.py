from test import calcule_somme

def test_calcule_somme_cinq():
    assert calcule_somme(5) == 15

def test_calcule_somme_dix():
    assert calcule_somme(10) == 55

def test_calcule_somme_un():
    assert calcule_somme(1) == 1

def test_calcule_somme_zero():
    assert calcule_somme(0) == 0

def test_calcule_somme_negatif():
    assert calcule_somme(-5) == 0
