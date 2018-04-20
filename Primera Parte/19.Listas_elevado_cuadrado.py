"""
Ejercicio19.Realizar un programa que reciba un conjunto de 5 números separados por comas 
e imprima una lista con los números elevados al cuadrado.
"""
i=0
lista2=[]
numero=0
numero_dos=0
# -*- coding: utf-8 -*-
print 'Ingresa una serie de 5 numeros separados por ",": '
cadena = raw_input('Ingrese cadena: ')
lista = cadena.split(",")
print 'Lista: ', lista[0:5]
print 'Lista al cuadrado: ',
while (i<5):
    numero=lista[i]
    numero_dos=int(numero)
    lista2.append(numero_dos**2)
    i=i+1

print lista2[0:5]
