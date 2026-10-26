#!/usr/bin/env python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

a=2
b=0
safe_print_division(a, b)
