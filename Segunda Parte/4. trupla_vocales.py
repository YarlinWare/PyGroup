"""
Ejercicio 4: Escribir un script que, dada una tupla de vocales, solicite al usuario
ingresar un car�cter y, realizando una comparaci�n con cada elemento de
la tupla establezca si el car�cter insertado es una vocal o no
"""
# -*- coding: utf-8 -*-
tupla_vocales = ("a", "e", "i", "o", "u","A", "E", "I", "O", "U")

letra = raw_input("Ingrese un car�cter: ")
i=0
for x in tupla_vocales:
    if(x==letra):
        print "La letra ingresada corresponde a una vocal"
    else:
        i=i+1

if(i==10):
     print "La letra ingresada corresponde a una constante"


    
        







