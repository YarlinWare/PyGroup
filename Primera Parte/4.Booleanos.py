"""
Ejercicio18.Por medio del uso de listas, realizar un programa que reciba
un conjunto de números separados por comas y sumen los números positivos
y los negativos aparte.
"""
# -*- coding: utf-8 -*-
print 'Ingrese 1.(True) ó 0.(False): '
operando_uno = int(raw_input('Ingrese valor: '))
operando_dos = int(raw_input('Ingrese valor: '))

operando1 = bool(operando_uno)
operando2 = bool(operando_dos)
print"\n-------***   Texto   ***-------\n"
print '\tAND: ',(operando1 and operando2)
print '\tOR:  ',(operando1 or operando2)
print '\tXOR: ',(operando1 ^ operando2)
print"\n-------***  Números  ***-------\n"
print '\tAND: ',(operando_uno and operando_dos)
print '\tOR:  ',(operando_uno or operando_dos)
print '\tXOR: ',(operando_uno ^ operando_dos)
print"\n-------***           ***-------\n"
