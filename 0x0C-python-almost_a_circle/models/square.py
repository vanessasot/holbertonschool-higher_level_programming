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
