# 
#  elif: opcionMenu == "2":
import os
from io import open  # libreria

archivo_texto = open("numeross.txt", "r") # r para leer el archivo
lineas=archivo_texto.readlines()
texto = archivo_texto.read() # se abre el archivo y se lee

archivo_texto.close() # cerramos el archivo

print(texto)

def invertir(s):
    return s[::-1]
def ordenar(s):
    a=sorted(s)
    s=''.join(a)
    return s
def kaprekar(numero,bucles): 
    #el metodo kaprekar usará las ventajas de la recursividad
    largoFaltante=4-len(numero) 
    #calculamos el largo faltante del string para cumplir con las 4 cifras
    invertir(numero)
    #invertimos el numero para hacer mas corta la concatenación
    if(largoFaltante!=0):
        for x in range(0, largoFaltante):
            numero+="0"
    numero=ordenar(numero)

    inv=int(numero)
    numero=int(invertir(numero))
    #convertimos los strings en numeros
    if(numero-inv==0):
        print("numero Invalido:")
        pass
    #nos aseguramos de que no sea un numero invalido como 1111
    
    else:
        if(inv-numero==6174 or numero-inv==6174):
            bucles=bucles+1
            print("funciono:"+' la cantidad de bucles fue de : '+str(bucles))
            pass 
        #checkeamos que no sea la constante de kapekar
        else:
            #si no lo es correremos nuevamente el bucle, sumando uno a la cantidad de iteraciones.
            if(inv-numero>0):
                bucles=bucles+1
                aux=inv-numero
                kaprekar(str(aux),bucles)
                
                pass
            else:       
                bucles=bucles+1
                aux=numero-inv
                kaprekar(str(aux), bucles)
                pass
        pass
        
pass 
#codigo del otro archivo
os.system('clear')

def menu():

    print(" selecciona una opcion ")
    print(" \t1 - 1ra opcion ") # opcion de ingresar un numero 
    print(" \t2 - 2da opcion ") # opcion atraves de un archivo txt
while True:
    opcionMenu=0
    menu()
    opcionMenu = input( " Ingrese la opcion: ")
    if(opcionMenu==1):
        print("Ingrese un numero :")
        numero=input()
        kaprekar(numero,0) 
        pass
    else:
      # cantidad=int(texto.readline())
       
        count=0
        for line in lineas: 
          
            print(line.strip())
            if(count>0):
                kaprekar(line.strip(),0)
                pass
            count += 1
        pass
