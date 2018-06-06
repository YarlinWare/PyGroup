"""
Ejercicio 3: Escribir un script que, dada una lista de números complejos, guarde en
una segunda lista el doble de la parte real, y en una tercer lista el triple de
la parte imaginaria de cada número. (Usar listas por comprensión)
"""
# -*- coding: utf-8 -*-
#convertir a numeros complejos
c1 = complex(2, 5)
c2 = complex(3, -10)
c3 = complex(1, 1)
c4 = complex(2, -1)
c5 = complex(2, 1)

#creamos lista con numeros complejos
list_num_complejos=[c1,c2,c3,c4,c5]
#multiplicamos cada elemento por 2
list_doble=[x*2 for x in list_num_complejos]
#multiplicamos cada elemento por 3
list_triple=[x*3 for x in list_num_complejos]

#imprimirmos resultados
print"Lista original: ", list_num_complejos
print"Lista doble:    ", list_doble
print"Lista triple:   ", list_triple






