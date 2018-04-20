"""
Ejercicio21.
Escribe un programa que reciba un conjunto de números e imprima cual es la 
suma de aquellos que se encuentran en posiciones pares.
"""
i=0
lista2=[]
suma=0
# -*- coding: utf-8 -*-
print 'Ingresa una serie de numeros separados por ",": '
cadena = raw_input('Ingrese cadena: ')
lista = cadena.split(",")

while(i<len(lista)):
    lista2.append(int(lista[i]))
    i=i+1
    
print 'Lista completa: \t', lista2[0:(len(lista))]
i=1
while(i<=len(lista)):
    if((i%2)!=0):
        suma = suma+lista2[i]
    i=i+1

print "Suma de posiciones pares: ",suma
    
