#!/usr/bin/python3
"""Create the module"""
from models.base import Base


class Rectangle(Base):
    """Create class Rectangle that heritance of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Value to width"""
        self.__width = width

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Value to height"""
        self.__height = height

    @property
    def x(self):
        """X"""
        return self.__x

    @x.setter
    def x(self, x):
        """Value to x"""
        self.__x = x

    @property
    def y(self):
        """Y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Value to y"""
        self.__y = y
