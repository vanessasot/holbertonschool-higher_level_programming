#!/usr/bin/python3
"""Module of Rectangle"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the instance."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Create a property"""
        return self.__width

    @width.setter
    def width(self, width):
        """Create setter"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Create a property"""
        return self.__height

    @height.setter
    def height(self, height):
        """Create setter"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculate area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints rectangle"""
        see = ""
        if self.__width == 0 or self.__height == 0:
            return see
        for i in range(self.__height):
            for j in range(self.__width):
                see = see + "#"
            if i != self.__height - 1:
                see = see + "\n"
        return see
