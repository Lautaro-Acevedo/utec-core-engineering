#!/usr/bin/env python3
"""
Módulo que proporciona una función para añadir texto
al final de un archivo.
"""


def append_write(filename="", text=""):
    """
    Añade una cadena al final de un archivo de texto (UTF-8),
    creándolo si no existe, y devuelve el número de
    caracteres añadidos.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
