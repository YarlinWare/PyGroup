"""
Ejercicio 20: Escribir un programa que, dada una tupla de n�meros del -5 al 5,
genere una tupla en la cual en la primer posici�n est� la suma de los n�meros positivos,
y en la segunda posici�n est� la suma de los n�meros negativos.
"""
# -*- coding: utf-8 -*-
tupla=(-5,-4,-3,-2,-1,0,1,2,3,4,5)
sumau=0
sumad=0
#--------------------------Suma Cuadrados-----------------------------
tupla_dos = ([x for x in tupla if (x<0)],[x for x in tupla if (x>0)])

for x in tupla:
    if(x<0):
        sumau=sumau+x
    else:
        sumad=sumad+x
    
tupla_tres = (sumau,sumad)
print "Tupla 1: ",tupla
print "Tupla 2: ",tupla_tres


    
