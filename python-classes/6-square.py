#!/usr/bin/python3
'''Write a class Square that defines a square by: (based on 5-square.py)'''


class Square:
    '''square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        x = self.__size ** 2
        return x

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''setter size'''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        x = self.size
        if x == 0:
            print('')
        else:
            p = self.position
            if p[1] > 0:
                print('\n' * p[1], end='')
            for i in range(x):
                print(' ' * p[0] + '#' * x)
