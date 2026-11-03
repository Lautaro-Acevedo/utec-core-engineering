#!/usr/bin/env python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con tamaño y posición opcionales."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el valor de size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el valor de size con validaciones."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera el valor de position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece el valor de position con validaciones estrictas."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def __str__(self):
        """Define la representación en cadena del objeto (para print())."""
        if self.__size == 0:
            return ""

        # position[1] define las líneas vacías verticales en la parte superior
        result = "\n" * self.__position[1]

        # position[0] define los espacios horizontales (sangría) a la izquierda de cada fila
        row_prefix = " " * self.__position[0]
        rows = [row_prefix + "#" * self.__size for _ in range(self.__size)]

        return result + "\n".join(rows)

    def my_print(self):
        """Imprime en stdout el cuadrado utilizando __str__."""
        print(self)
