#!/usr/bin/python3
''' Write a function that divides all elements of a matrix '''


def matrix_divided(matrix, div):
    ''' div matrix '''
    new_matrix = []
    message = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in matrix:
        new = []
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(message)
            res = j / div
            new.append(round(res, 2))
        new_matrix.append(new)
    return new_matrix
