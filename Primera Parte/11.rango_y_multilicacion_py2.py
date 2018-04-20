# -*- coding: utf-8 -*-
"""
Ejercicio11.Escribe un programa que reciba dos números para crear un rango y multiplique los
números dentro del rango, sin incluir el número final de éste. Ejemplo: Inicio = 2,
Final 5. Resultado = 2*3*4 = 24."""
inicio = int(raw_input('Ingrese un primer valor:\t'))
final = int(raw_input("Ingrese un segundo valor:\t"))
i=1
while inicio < final:
    i *= (inicio)
    print " ", inicio
    inicio += 1

print "resultado: ", i
