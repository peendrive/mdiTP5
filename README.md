# mdiTP5
Trabajo practico sobre la constante de Kaprekar
k=constante de kaprekar
num= numero a checkear
if(num==k)-> 8
else-> _kaprekar(num){
    generar inverso-> inv
    checkear que el inverso no sea igual al numero original (para evitar 1111 y similares)
    num-inv=posible
    if posible>0{
        _kaprekar(posible)
    }else{
        _kaprekar(inv-num)
    }
    
}