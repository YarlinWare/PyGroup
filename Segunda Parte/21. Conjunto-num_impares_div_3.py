"""
Ejercicio 21: Redactar un script el cual genere un conjunto usando conjuntos
por comprensión con los números del 1 al 21 que sean impares y
que sean divisible por 3.
"""
# -*- coding: utf-8 -*-
conjunto={x for x in range(1,22) if (x%3==0 and x%2==1)}
print "Conjunto: ",conjunto
