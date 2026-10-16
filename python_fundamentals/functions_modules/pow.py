#!/usr/bin/env python3

# definimos funcion
def pow(a, b):
    # Todo numero elevado a la 0 da 1
    if b == 0:
        return 1
    # Si b es negativo obtenemos su exponente
    result = 1
    exp = b if b > 0 else -b
    # Se multiplica tantas veces (a) como lo indique el exponente
    for _ in range(exp):
        result *= a

    if b < 0:
        return 1 / result
    return result
