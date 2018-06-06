"""
Ejercicio 17: Diseñar un programa que pregunte al usuario si desea continuar, en caso
afirmativo imprima los números del 1 al 10 y vuelva a hacer la pregunta,
en caso afirmativo de nuevo imprima los números del 11 al 20 y vuelva a
hacer la pregunta, y así sucesivamente hasta una respuesta negativa.
"""
# -*- coding: utf-8 -*-

respuesta=1
x=0
k=x
final=10
suma=0
while (respuesta!=0):
    respuesta = int(raw_input("""Desea continuar en el programa:
    0. No
    1. Si
    R/: """))
    if(respuesta != 0):
        for x in range(k,final+1) :
            print x,",",
        print " "
        k=final
        final=final+10       
        respuesta=1
    else:
        break
    
    
 

    
