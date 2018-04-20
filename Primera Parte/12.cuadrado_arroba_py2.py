"""
Ejercicio12:Escribe un programa que reciba un número e imprima un cuadrado de arrobas de
tamaño según el número ingresado. (Se debe imprimir el borde y el relleno).
"""
# -*- coding: utf-8 -*-
lado = int(raw_input('Ingrese tamaño de un lado del cuadrado: '))
for j in range(lado):
    for i in range(lado):
        print "@",
    print ""
    
    
