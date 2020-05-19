def kaprekar(numero,bucles):
    
    largoFaltante=4-len(numero)
    invertir(numero)
    for x in range(0, largoFaltante):
        numero+="0"
    inv=int(invertir(numero))
    numero=int(numero)
    if(inv-numero==6174 or numero-inv==6174):
        print("funciono"+bucles)
        pass 
    else:
        if(inv-numero>0):
            bucles=bucles+1
            kaprekar(str(inv-numero),bucles)
            pass
        else:       
            bucles=bucles+1
            kaprekar(str(numero-inv), bucles)
            pass
    pass
        
pass

def invertir(s):
    return s[::-1]

bucles=0
print("Ingrese un numero :")
numero=input()
kaprekar(numero,bucles)
