"""
Ejercicio 6: Hacer un programa que dados dos conjuntos, realice la unión, la
intersección, la diferencia, la diferencia simétrica y guarde los
resultados en una lista.
"""
# -*- coding: utf-8 -*-

conjunto_1 = {3, 4, 10, 11, 12, 5, 2}
conjunto_2 = {2, 3, 4, 5, 6, 7, 8}

#----------------------------Conjuntos---------------------------------
print "Conjunto 1: ", conjunto_1
print "Conjunto 2: ", conjunto_2

#----------------------------Unión-------------------------------------
print "Unión: ",conjunto_1 | conjunto_2
#print "Unión: ",conjunto_1.union(conjunto_2)

#----------------------------Interseción-------------------------------
print "Intersección: ",conjunto_1 & conjunto_2
#print "Intersección: ",conjunto_1.intersection(conjunto_2)

#----------------------------Diferencia--------------------------------
print "Diferencia: ",conjunto_1 - conjunto_2
#print "Diferencia: ",conjunto_1.difference(conjunto_2)

#----------------------------Diferencia simétrica----------------------
print "Diferencia simétrica: ", conjunto_1 ^ conjunto_2
#print "Unión exclusiva: ", conjunto_1.symmetric_difference(conjunto_2)
#----------------------------------------------------------------------
    
        







