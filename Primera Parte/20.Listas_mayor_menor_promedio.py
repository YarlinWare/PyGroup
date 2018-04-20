import decimal
from decimal import Decimal, getcontext
"""
Ejercicio20.Escribe un programa que reciba un conjunto de números separados por
comas y determine en que posición se encuentra el mayor, el menor y el que se
acerque al promedio.
"""
i=0
lista2=[]
# -*- coding: utf-8 -*-
print 'Ingresa una serie de 5 numeros separados por ",": '
cadena = raw_input('Ingrese cadena: ')
lista = cadena.split(",")
print 'Lista: ', lista[0:5]

while(i<5):
    lista2.append(int(lista[i]))
    i=i+1
    
mayor=lista2[0]
menor=lista2[0]
promedio=lista2[0]
i=1
while(i<5):
    if (lista2[i]>= mayor):
        mayor = lista2[i]
    if (lista2[i]< menor):
        menor = lista2[i]
    promedio= Decimal(promedio + lista2[i])
    i=i+1
    
promedio = Decimal(promedio / len(lista2))
print 'mayor: \t\t', mayor, '\nmenor: \t\t', menor, '\npromedio: \t', promedio
