"""
Ejercicio 23: Escribir un programa que dado un diccionario de 5 nombres cuyas
claves son los números del 1 al 5 establezca cuál es el nombre de
mayor longitud y diga cuál es su clave.
"""
# -*- coding: utf-8 -*-
maximo=0
valor=0
posicion=0
nombre=""
nombre_1 = raw_input("Ingrese nombre 1: ")
nombre_2 = raw_input("Ingrese nombre 2: ")
nombre_3 = raw_input("Ingrese nombre 3: ")
nombre_4 = raw_input("Ingrese nombre 4: ")
nombre_5 = raw_input("Ingrese nombre 5: ")

diccionario = {nombre_1:1,nombre_2:2,nombre_3:3,nombre_4:4,nombre_5:5}

for x in diccionario:
    valor=len(x)
    if valor>=maximo:
        maximo=valor
        posicion=x
    else:
        maximo=maximo
    print "Lingitud ",x," es: ", len(x)

print"Diccionario: ",diccionario
print"El valor del nombre de mayor longitud es: ",diccionario[posicion]

