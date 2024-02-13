# test_jeu_devinette.py

from unittest.mock import patch
from jeu_devinette_de_nbr import jeu_devinette

# Test quand le joueur propose un nombre inférieur à la valeur réelle
@patch('builtins.input', side_effect=['50', '70', 'Non'])
@patch('random.randint', return_value=70)
def test_jeu_devinette_low_guess(mock_randint, mock_input, capsys):
    jeu_devinette()
    captured = capsys.readouterr()
    assert "Le nombre que je pense est plus grand!" in captured.out
    assert "Merci d'avoir joué!" in captured.out

# Test quand le joueur propose un nombre supérieur à la valeur réelle
@patch('builtins.input', side_effect=['50', '30', 'Non'])
@patch('random.randint', return_value=30)
def test_jeu_devinette_high_guess(mock_randint, mock_input, capsys):
    jeu_devinette()
    captured = capsys.readouterr()
    assert "Le nombre que je pense est plus petit!" in captured.out
    assert "Merci d'avoir joué!" in captured.out

# Test quand le joueur devine correctement le nombre
@patch('builtins.input', side_effect=['50', 'Non'])
@patch('random.randint', return_value=50)
def test_jeu_devinette_correct_guess(mock_randint, mock_input, capsys):
    jeu_devinette()
    captured = capsys.readouterr()
    assert 'Félicitations! Vous avez deviné le nombre en 1 essais!' in captured.out
    assert "Merci d'avoir joué!" in captured.out