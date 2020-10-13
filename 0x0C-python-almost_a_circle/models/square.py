#!/usr/bin/python3
"""Create the module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create the square class heritance of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the value"""
        return self.width

    @size.setter
    def size(self, size):
        """Size value"""
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - "\
               "{}". format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.size = args[arg]
                if arg == 2:
                    self.x = args[arg]
                if arg == 3:
                    self.y = args[arg]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
