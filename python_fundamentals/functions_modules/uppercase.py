#!/usr/bin/env python3
#definicion de funcion
def uppercase(str):
    new_str = ""
    #recorre la cadena caracter por caracter
    for c in str:
        if 97 <= ord(c) <= 122:
            #convierte el caracter en mayuscula
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print("{}".format(new_str))
