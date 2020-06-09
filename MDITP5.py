


import os
from io import open  # libreria
"""
archivo_texto = open("numeross.txt", "r") # r para leer el archivo
lineas=archivo_texto.readlines()
texto = archivo_texto.read() # se abre el archivo y se lee
archivo_texto.close() # cerramos el archivo
print(texto)
"""
tab = []
loop = 'loop'

print (" Vamos a comenzar.. ")
inicio = input(" Escribe empezar para iniciar el programa ")
while (inicio == 'empezar') :

    print (""" ¿que camino quieres hacer?  1 - Ingresar numero para la constante  2 - Obtener un saludo """)
    opcion = input()     
    
    if opcion == '1':

        # ordeno de forma ascendente
        def ascendente(numero):
            return int(''.join(sorted(str(numero))))
 
        # ordeno de forma descendente
        def descendente(numero):
            return int(''.join(sorted(str(numero))[::-1]))

         # pido ungresar el numero
        numero = input(" ingrese un numero de 4 cifras ")
        try:
            n = int(numero)
        except :
            print("\nnumero invalido!!!\nasumiendo que numero = 2016.")
            n = "2016"
        print("\ntransformando", str(n) + ":")
            
            #print ("\n transformado", numero)

          #  itero y asigno numeros
        while numero != descendente(numero) - ascendente(numero):
                print (descendente(numero), "-", ascendente(numero), "=", descendente(numero)-ascendente(numero))
                numero = descendente(numero) - ascendente(numero)
        if n not in tab:
        
            tab.append(numero)
        else:
            if tab.index(numero) == len(tab)-1:
        # encuentro el numero a la constante
                tab = []
                tab.append(numero)
                loop = 'constant'
            else:
        
                tab = tab[tab.index(numero):]
            
            pass
        print ("constante de Kaprekar :", numero)
        print(" Gracias por usar el programa..!! ")
    elif opcion == '2':
        print(" Que tengas un buen dia..!!! ")
        print(" Gracias por usar el programa..!! ")

