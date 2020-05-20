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

bucles=0
print("Ingrese un numero :")
numero=input()
kaprekar(numero,bucles)
