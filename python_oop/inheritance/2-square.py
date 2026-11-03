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
        """Return the print() and str() representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
