#!/usr/bin/python3
"""Module of square size."""


class Square:
    """Class square size."""

    def __init__(self, size=0):
        """Initialize the instance."""
        self.__size = size

    @property
    def size(self):
        """Create a property"""
        return self.__size

    @size.setter
    def size(self, size):
        """Create setter"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Create area method"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Create my_print method"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
