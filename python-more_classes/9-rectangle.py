#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    init
    """
    number_of_instances = 0

    print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1

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

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
