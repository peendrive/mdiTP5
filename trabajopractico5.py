





n = int(input(""" Vamos a comenzar... \n Ingrese el numero de 4 digintos para empezar: """))
grande = 0
chico = 0
contador = 0
tab = []
tab1 = []
tab2 = []
tab.append(n)




if len(str(n)) != 4:
    print("El numero ingresado no es valido.")
   
else:
    
    while(n != 6174):
        
        for i in str(n):
            tab1.append(i)
        
        for j in str(n):
            tab2.append(j)
        
        for recorrido in range(1,len(tab1)):
            for posicion in range(len(tab1) - recorrido):
                if tab1[posicion] > tab1[posicion + 1]:
                    aux = tab1[posicion]
                    tab1[posicion] = tab1[posicion + 1]
                    tab1[posicion + 1] = aux
        
        for recorrido in range(1,len(tab2)):
            for posicion in range(len(tab2) - recorrido):
                if tab2[posicion] < tab2[posicion + 1]:
                    aux = tab2[posicion]
                    tab2[posicion] = tab2[posicion + 1]
                    tab2[posicion + 1] = aux

        chico = "".join(tab1)
        grande = "".join(tab2)
        print("Numero actual: " + str(n))
        print("Numero menor posible: " + chico)
        print("Numero mayor posible: " + grande)
        print("")
        
        tab = []
        tab1 = []
        tab2 = []
        n = int(grande)-int(chico)
        contador += 1
    
    print("El numero ingresado alcanzo el numero de Keprekar luego de " + str(contador) + " iteraciones ")
    print(" Gracias por haber usado el programa ")
    print(" Que tengas buen dia ")





