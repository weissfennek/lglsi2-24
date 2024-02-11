import pytest
from mot_palindrome import est_palindrome

# List of words to test
words = ["radar", "python", "stats", "level", "deified"]

@pytest.mark.parametrize("word, expected", [
    ("radar", True),
    ("python", False),
    ("stats", True),
    ("level", True),
    ("deified", True)
])
def test_palindrome_detection(word, expected):
    assert est_palindrome(word) == expected
