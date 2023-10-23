#!/usr/bin/python3
"""
Task 12 module
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    result = []

    if n <= 0:
        return result

    result.append([1])

    for i in range(1, n):
        result.append([1])
        for j in range(1, i + 1):
            try:
                result[i].append(result[i - 1][j] + result[i - 1][j - 1])
            except IndexError:
                result[i].append(1)
                continue

    return(result)
