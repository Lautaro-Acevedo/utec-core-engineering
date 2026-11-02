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

    def area(self):
        """Calcula el area del cuadrado"""
        size = self.__size
        return size * size

    @property
    def size(self):
        """Devuelve la cantidad de entradas."""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """imprime un cuadrado con #"""
        if self.__size == 0:
            print("")
            return
        """
        Creamos las filas multiplicando el 
        símbolo por el tamaño y las unimos con '\n' 
        """
        rows = ["#" * self.__size for _ in range(self.__size)]
        print("\n".join(rows))
