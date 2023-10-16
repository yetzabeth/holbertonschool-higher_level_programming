#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Class that define a BaseGeometry object"""
    pass

    def area(self):
        """Calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        # we can assume @name is always a string
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Class that define a new class based on BaseGeometry class"""

    def __init__(self, width, height):
        """To create a new instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__heigth

    def __str__(self):
        return print("[Rectangle] {}/{}".format(self.__width, self.__heigth))
