import pytest

from somme_carres_pairs import carre,somme_carres_pairs

def test_carre():
    assert carre(2) == 4
    assert carre(3) == 9
    assert carre(0) == 0
    assert carre(-2)== 4


def test_somme_carres_pairs():
    assert somme_carres_pairs(10) == 220
    assert somme_carres_pairs(0) == 0
    assert somme_carres_pairs(2) == 4
    assert somme_carres_pairs(-2) == 0
    
