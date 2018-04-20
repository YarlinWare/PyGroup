
"""
Ejercicio13:Escribe un programa que reciba un numero e imprima un cuadrado de arrobas de
tamaño segun el numero ingresado. (Solo se debe imprimir el exterior, el borde)
"""
# -*- coding: utf-8 -*-
lado = int(raw_input('Ingrese tamaño de un lado del cuadrado: '))
for i in range(lado):
    for j in range(lado):        
        if (i>0 and i<lado-1)and(j>0 and j<lado-1):
            print " ",        
        else:
            print "x",
    print ""
    
    
