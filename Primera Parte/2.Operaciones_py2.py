
import decimal
from decimal import Decimal, getcontext
"""
Ejercicio1:Escribe un programa que reciba dos n�meros y los sume, los reste, los multiplique,
realice una divisi�n entera y una divisi�n con resultado decimal sobre ellos,
adem�s de mostrar el residuo de la divisi�n.
"""
# -*- coding: utf-8 -*-
a = int(raw_input('Ingrese primer valor: '))
b = int(raw_input('Ingrese segundo valor: '))
suma = a + b
resta = a - b
multiplicacion = a * b

print 'La suma de ' , a ,'+' , b , ' es:     \t' , suma
print 'La resta de ' , a ,'-' , b , ' es: \t', resta
print 'El producto de ' , a , 'X' , b , ' es: \t', multiplicacion

if a == 0 or b == 0:
    print 'La divisi�n en este caso, no es posible...'
else:

    division = Decimal(a) / Decimal(b)
    div_entera = (a//b)
    residuo = a % b
    print 'La divisi�n de ' , a , '/' , b , ' es: \t', division
    print 'La divisi�n entera de ' , a , '/' , b , ' es: \t', div_entera , ' y su residuo es: ' , residuo



