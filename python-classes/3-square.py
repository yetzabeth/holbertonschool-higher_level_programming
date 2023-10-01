#!/usr/bin/python3
'''Write a class Square that defines a square'''


class Square():
    '''square class'''
    def __init__(self, size=0):
        if not (type(size) == int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        x = self.__size ** 2
        return x
