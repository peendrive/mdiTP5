# 
#  elif: opcionMenu == "2":

import os
from io import open  # libreria

archivo_texto = open("numeross.txt", "r") # r para leer el archivo

texto = archivo_texto.read() # se abre el archivo y se lee

archivo_texto.close() # cerramos el archivo

print(texto)

"""
def menu():
    os.system('cls')
    print(" selecciona una opcion ")
    print(" \t1 - 1ra opcion ") # opcion de ingresar un numero 
    print(" \t2 - 2da opcion ") # opcion atraves de un archivo txt

while True:
    menu()
    opcionMenu = input( " ingresa el valor ")


def ascendente(numero) :
    return int(''.join(sorted(str(num-inv))))

def descendente(numero) :
   return int(''.join(sorted(str(num-inv))[::-1]))



while True:
   
    numero = texto
    print(descendente(numero), "-", ascendente(numero), "=", descendente(numero)-ascendente(numero))
    numero = descendente(numero) - ascendente(numero)


    if i not in tex:
        tex.append(num-inv)
    else:
        if tex.index(num-inv) == len(tex)-1:
            tex = []
            tex.append(num-inv)
            loop = 'constant'
        else:
            tex = tex[tex.index(numeros):]
        break

print('Kaprekar', loop, 'reached:', tex)
"""

