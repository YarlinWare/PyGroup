"""
Ejercicio 19: Escribir un programa que muestre la suma de los cuadrados de los
números del 1 al 100
"""
# -*- coding: utf-8 -*-
suma=0
#--------------------------Suma Cuadrados-----------------------------
print "--------------------------Suma Cuadrados 1 al 100-----------------------------"
lista =[x**2 for x in range(1,101)]
print " "
print "Lista números pares:   ",lista
print " "
for x in lista:
    suma = suma + x    
print "La suma de los números pares es: ",suma
print " "



    
