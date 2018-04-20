

"""
Ejercicio5:Escribe un programa que determine si un número es par o impar.
"""
# -*- coding: utf-8 -*-
a= int(raw_input("Ingrese un valor entero: "))
par = a%2
if (par == 0):
   print "El número ingresado es par"
else:
    print "El número ingresado es impar"
