#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new_row = [j**2 for j in i]
        new.append(new_row)
    return new
