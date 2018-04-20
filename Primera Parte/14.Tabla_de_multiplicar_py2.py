"""
Ejercicio14:Escribe un programa que reciba un número e imprima las tablas de multiplicar
hasta dicho número en forma de cuadrícula. Por ejemplo: Número ingresado: 3
"""
# -*- coding: utf-8 -*-
numero = int(raw_input('Ingrese número: '))
i=1
j=1
for i in range(numero+1):
    for j in range(numero+1):
        if(i>0 and j>0):
            print (i*j),"\t",
        else:
            print ""
    print ""
        
  
    
    
