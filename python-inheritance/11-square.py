#!/usr/bin/python3
"""Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class based on Rectangle baseclass"""

    def __init__(self, size):
        """To create a new instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
