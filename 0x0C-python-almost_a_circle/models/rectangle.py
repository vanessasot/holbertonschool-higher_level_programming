#!/usr/bin/python3
"""Create the module"""
from models.base import Base


class Rectangle(Base):
    """Create class Rectangle that heritance of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Value to width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Value to height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X"""
        return self.__x

    @x.setter
    def x(self, x):
        """Value to x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Value to y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate area the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for l in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Print data"""
        return "[Rectangle] ({}) {}/{} - "\
               "{}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Assigns an argument to each attribute"""
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.__width = args[arg]
                if arg == 2:
                    self.__height = args[arg]
                if arg == 3:
                    self.__x = args[arg]
                if arg == 4:
                    self.__y = args[arg]
