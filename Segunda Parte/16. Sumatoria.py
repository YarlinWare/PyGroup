"""
Ejercicio 16: Escribir un script que solicite al usuario un n�mero, y que imprima la
sumatoria de los n�meros del 1 hasta el n�mero ingresado.
"""
# -*- coding: utf-8 -*-
final = int(raw_input("Indique hasta que valor desea realizar la sumatoria: "))

while(final <=0):
    final = int(raw_input("Indique hasta que valor desea realizar la sumatoria: "))
suma=0   
for x in range(1,final+1) :
    suma=suma+x    

print "La sumatoria de ", final," es: ",suma               
 

    
