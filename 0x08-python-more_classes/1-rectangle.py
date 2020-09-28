#!/usr/bin/python3
"""Module of Rectangle"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the instance."""

        self.__width = width
        self.__height = height

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
