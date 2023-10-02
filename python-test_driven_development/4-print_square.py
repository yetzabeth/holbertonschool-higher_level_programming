#!/usr/bin/python3
''' print a square '''


def print_square(size):
    '''print a square'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print('')
