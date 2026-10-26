#!/usr/bin/env python3
"""
Módulo que proporciona una función para leer y mostrar
el contenido de un archivo de texto en codificación UTF-8.
"""


def read_file(filename=""):
    """
    Lee un archivo de texto (UTF-8) utilizando la sentencia 'with'
    y lo imprime directamente en la salida estándar (stdout).
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
