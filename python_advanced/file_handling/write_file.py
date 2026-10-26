#!/usr/bin/env python3
"""
Módulo que proporciona una función para escribir
cadenas de texto en un archivo.
"""


def write_file(filename="", text=""):
    """
    Escribe una cadena de texto en un archivo de texto (UTF-8),
    creándolo si no existe o sobrescribiéndolo si ya existe,
    y devuelve el número de caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
