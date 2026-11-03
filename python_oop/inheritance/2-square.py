#!/usr/bin/env python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the print() and str() representation."""
        w = self._Rectangle__width
        h = self._Rectangle__height
        return "[Square] {}/{}".format(w, h)
