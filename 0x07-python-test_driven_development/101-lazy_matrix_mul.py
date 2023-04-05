#!/usr/bin/python3

"""

Module composed by a function that multiplies 2 matrices

"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Validate inputs
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if m_a == [] or m_b == []:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    m_a_np = np.array(m_a)
    m_b_np = np.array(m_b)
    result = np.matmul(m_a_np, m_b_np)
    return result.tolist()
