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
    def size(self, size):
        """Create setter"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Create a property"""
        return self.__position

    @position.setter
    def position(self, position):
        """Create setter"""
        if type(position) is not tuple or len(position) != 2 or \
            type(position[0]) is not int or position[0] < 0 or \
                type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Create area method"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Create my_print method"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
