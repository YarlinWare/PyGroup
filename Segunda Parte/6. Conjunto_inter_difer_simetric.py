"""
Ejercicio 6: Hacer un programa que dados dos conjuntos, realice la uni�n, la
intersecci�n, la diferencia, la diferencia sim�trica y guarde los
resultados en una lista.
"""
# -*- coding: utf-8 -*-

conjunto_1 = {3, 4, 10, 11, 12, 5, 2}
conjunto_2 = {2, 3, 4, 5, 6, 7, 8}

#----------------------------Conjuntos---------------------------------
print "Conjunto 1: ", conjunto_1
print "Conjunto 2: ", conjunto_2

#----------------------------Uni�n-------------------------------------
print "Uni�n: ",conjunto_1 | conjunto_2
#print "Uni�n: ",conjunto_1.union(conjunto_2)

#----------------------------Interseci�n-------------------------------
print "Intersecci�n: ",conjunto_1 & conjunto_2
#print "Intersecci�n: ",conjunto_1.intersection(conjunto_2)

#----------------------------Diferencia--------------------------------
print "Diferencia: ",conjunto_1 - conjunto_2
#print "Diferencia: ",conjunto_1.difference(conjunto_2)

#----------------------------Diferencia sim�trica----------------------
print "Diferencia sim�trica: ", conjunto_1 ^ conjunto_2
#print "Uni�n exclusiva: ", conjunto_1.symmetric_difference(conjunto_2)
#----------------------------------------------------------------------
    
        







