"""
Ejercicio 5: Escribir un script que, dada una lista de números complejos,
genere un diccionario cuya clave sea la parte real y cuyo valor sea
la parte imaginaria de cada número.
"""
# -*- coding: utf-8 -*-

c1 = complex(1, 1)
c2 = complex(5, -6)
c3 = complex(4, 5)
c4 = complex(2, 5)
c5 = complex(3, -10)

list_num_complejos=[c1,c2,c3,c4,c5]

diccionario_num_complejos={x.real: x.imag for x in list_num_complejos}
print "Diccionario: ",diccionario_num_complejos





    
        







