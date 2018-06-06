"""
Ejercicio 18: Configurar un script que sume los números pares del 1 al 100 y
saque un promedio. De igual forma, con los impares.
"""
# -*- coding: utf-8 -*-
suma_par=0
suma_impar=0
#--------------------------Pares-----------------------------
print "--------------------------Pares-----------------------------"
pares =[x for x in range(1,101) if (x%2==0)]
print " "
print "Lista números pares:   ",pares
print " "
for x in pares:
    suma_par = suma_par + x    
print "La suma de los números pares es: ",suma_par
print " "

#-------------------------Impares----------------------------
print "-------------------------Impares----------------------------"
print " "
impares =[x for x in range(1,100) if (x%2==1)]
print "Lista números impares: ",impares
print " "
for x in impares:
    suma_impar=suma_impar+x    
print "La suma de los números impares es: ",suma_impar
print " "   
 
 

    
