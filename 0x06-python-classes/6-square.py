#!/usr/bin/python3
"""Module of square size."""


class Square:
    """Class square size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Create a property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Create setter"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Create a property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Create setter"""
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Create area method"""
        return self.__size ** 2

    def my_print(self):
        """Create my_print method"""
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
