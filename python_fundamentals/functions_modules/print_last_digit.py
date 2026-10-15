#!/usr/bin/env python3

# Imprime ul ultimo digito siempre positivo
def print_last_digit(number):
    if number < 0:
        # si es negativo con (-number) lo convertimos a positivo
        last_digit = (-number) % 10
    else:
        # Si es positivo tomamos el ultimo numero y lo imprimimos
        last_digit = number % 10
    print("{}".format(last_digit))
    return last_digit
