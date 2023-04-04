#!/usr/bin/python3

"""

This module is made by a function that divides the numbers of a matrix

"""

def matrix_divided(matrix, div):
    """ This function divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        
        ZeroDivisionError: If div is zero

    """

    def matrix_divided(matrix, div):
    # Check if matrix is valid
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have same length
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is valid
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix
    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]

    return new_matrix


