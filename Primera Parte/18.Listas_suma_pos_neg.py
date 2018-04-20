"""
Ejercicio18.Por medio del uso de listas, realizar un programa que reciba
un conjunto de números separados por comas y sumen los números positivos
y los negativos aparte.
"""
i=0
suma_pos=0
suma_neg=0
numero=0
numero_dos=0
# -*- coding: utf-8 -*-
print 'Ingresa una serie de 5 numeros separados por ",": '
cadena = raw_input('Ingrese cadena: ')
lista = cadena.split(",")
print 'Lista: ', lista[0:5]
while (i<5):
    numero=lista[i]
    numero_dos=int(numero)
    if(numero_dos>0):
        suma_pos=suma_pos+numero_dos
    else:
        suma_neg=suma_neg+numero_dos
    i=i+1
print 'Suma de los números positivos es: ',suma_pos
print 'Suma de los números negativos es: ',suma_neg
