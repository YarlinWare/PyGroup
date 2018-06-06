"""
Ejercicio 7: Generar un script que, dada una tupla de tuplas de 2 enteros,
genere números complejos con las tuplas de la tupla.
"""
# -*- coding: utf-8 -*-

tupla = ((1, 2), (3, 4), (5,6),(7,8))

print "Tupla: ", tupla
print "Complejos: (",
for x in tupla:
    for z in x:
        if (z%2==1):
            print complex(z,z+1)," ",
print ")",
        
    
