"""
Ejercicio 14: Escribir un script que haga la suma de los primeros 10 n�meros enteros
usando un ciclo for, un ciclo while, una lista por comprensi�n, una tupla
por comprensi�n y un conjunto por comprensi�n. (Nota: El resultado de
la lista, el conjunto y la tupla por comprensi�n debe ser similar a [0, 1, 3,
6, 10, 15, �, 45])
"""
# -*- coding: utf-8 -*-
x=0
print "While: "
while (x<=46):
    if (x%2==1):
        print x,
        if x<45:
            print ",",
        else:
            print " " 
    x=x+1
    
print " "
print " "
print "For: "
for x in range (1, 46):
    if (x%2==1):
        print x,
        if x<45:
            print ",",
        else:
            print " "
    
lista =[x for x in range(1,46) if (x%2==1)]
tupla =([x for x in range(1,46) if (x%2==1)])
conjunto ={x for x in range(1,46) if (x%2==1)}
print " "
print "Lista: "
print lista
print " "
print "Tupla: "
print tupla
print " "
print "Conjunto: "
print conjunto

    
