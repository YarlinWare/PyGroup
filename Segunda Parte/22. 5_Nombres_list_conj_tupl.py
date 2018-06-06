"""
Ejercicio 22: Diseñar un script que solicite al usuario 5 nombres y los guarde en
una tupla, una lista, y un conjunto.
"""
# -*- coding: utf-8 -*-

nombre_1 = raw_input("Ingrese nombre 1: ")
nombre_2 = raw_input("Ingrese nombre 2: ")
nombre_3 = raw_input("Ingrese nombre 3: ")
nombre_4 = raw_input("Ingrese nombre 4: ")
nombre_5 = raw_input("Ingrese nombre 5: ")

lista=[nombre_1,nombre_2,nombre_3,nombre_4,nombre_5]
tupla=(nombre_1,nombre_2,nombre_3,nombre_4,nombre_5)
conjunto={nombre_1,nombre_2,nombre_3,nombre_4,nombre_5}

print"Lista: ", lista
print"Tupla: ", tupla
print"Conjunto: ", conjunto
