"""
Ejercicio 9: Escribir un script que imprima los números del 1 al 10 pero de tipo
cadena. Para poder verificar que el tipo no sea entero, el programa
debe también imprimir el tipo de dato implicado.
"""
# -*- coding: utf-8 -*-

for x in range(11):
    k=str(x)    
    print "Número: ", k," ", 
    print "Tipo: ",type(k)

