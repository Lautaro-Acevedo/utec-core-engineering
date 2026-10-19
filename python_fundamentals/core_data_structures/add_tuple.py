#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Rellenamos las tuplas con ceros por si tienen menos de 2 elementos
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Sumamos los dos primeros elementos ignorando el resto
    return (a[0] + b[0], a[1] + b[1])
