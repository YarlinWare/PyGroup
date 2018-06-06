"""
Ejercicio 16: Escribir un script que solicite al usuario un número, y que imprima la
sumatoria de los números del 1 hasta el número ingresado.
"""
# -*- coding: utf-8 -*-
final = int(raw_input("Indique hasta que valor desea realizar la sumatoria: "))

while(final <=0):
    final = int(raw_input("Indique hasta que valor desea realizar la sumatoria: "))
suma=0   
for x in range(1,final+1) :
    suma=suma+x    

print "La sumatoria de ", final," es: ",suma               
 

    
