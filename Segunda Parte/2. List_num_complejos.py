"""
Ejercicio 2: Crear un programa que, dada una lista de números complejos, halle la
magnitud de cada uno y lo guarde en una nueva lista. (Usar listas por
comprensión sabiendo que abs() halla la magnitud de un solo número)
"""
# -*- coding: utf-8 -*-
c1 = complex(2, 5)
c2 = complex(3, -10)
c3 = complex(1, 1)
c4 = complex(2, -1)
c5 = complex(2, 1)

list_num_complejos=[c1,c2,c3,c4,c5]

magnitud=[abs(x) for x in list_num_complejos]

print"Lista de numeros complejos: ", list_num_complejos
print "Longitud: ", magnitud





