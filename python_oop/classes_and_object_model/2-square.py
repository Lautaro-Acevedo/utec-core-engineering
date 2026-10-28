#!/usr/bin/env python3
"""
Módulo 1-square
Definimos una clase Square con un atributo privado size.
"""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Representa un cuadrado con tamano."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
