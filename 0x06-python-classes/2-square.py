#!/usr/bin/python3
"""Module of square size."""


class Square:
    """Class square size."""

    def __init__(self, size=0):
        """Initialize the instance."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
