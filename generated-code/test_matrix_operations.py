import pytest
from matrix_operations import multiply_matrices


# Test case 1: Multiplying two 1x1 matrices
def test_multiply_matrices_1x1():
    mat1 = [[1]]
    mat2 = [[2]]
    result = multiply_matrices(mat1, mat2)
    assert result == [[2]], "Failed for 1x1 matrices"

# Test case 2: Multiplying two 2x2 matrices
def test_multiply_matrices_2x2():
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    result = multiply_matrices(mat1, mat2)
    assert result == [[19, 22], [43, 50]], "Failed for 2x2 matrices"

# Test case 3: Multiplying two 3x3 matrices
def test_multiply_matrices_3x3():
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    result = multiply_matrices(mat1, mat2)
    assert result == [[84, 90, 96], [201, 216, 231], [318, 342, 366]], "Failed for 3x3 matrices"

# Test case 4: Multiplying a 2x2 matrix with a 2x1 matrix
def test_multiply_matrices_2x2_2x1():
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5], [6]]
    result = multiply_matrices(mat1, mat2)
    assert result == [[17], [39]], "Failed for 2x2 with 2x1 matrices"

# Test case 5: Multiplying a 1x1 matrix with a 1x1 matrix
def test_multiply_matrices_1x1_1x1():
    mat1 = [[1]]
    mat2 = [[2]]
    result = multiply_matrices(mat1, mat2)
    assert result == [[2]], "Failed for 1x1 with 1x1 matrices"

# Test case 1: Attempting to multiply a 2x2 matrix with a 3x3 matrix
def test_multiply_matrices_2x2_3x3():
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
    with pytest.raises(ValueError):
        multiply_matrices(mat1, mat2)

# Test case 2: Attempting to multiply a 3x3 matrix with a 2x2 matrix
def test_multiply_matrices_3x3_2x2():
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[10, 11], [12, 13]]
    with pytest.raises(ValueError):
        multiply_matrices(mat1, mat2)

