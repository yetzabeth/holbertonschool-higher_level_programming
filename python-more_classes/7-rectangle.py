#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    init
    """
    number_of_instances = 0
    print_symbol = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            per = (self.width * 2) + (self.height * 2)
            return per

    def __str__(self):
        print_rec = ''
        if self.width == 0 or self.height == 0:
            return ''
        for i in range(self.height):
            for j in range(self.width):
                print_rec += str(self.print_symbol)
            print_rec += '\n'
        temp = print_rec[:-1]
        return temp

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Setter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
