"""
Ejercicio17.Escribe un programa que reciba un conjunto de cadenas e imprima
cuál es la de mayor longitud y en qué posición se encuentra.
"""
# -*- coding: utf-8 -*-
cantidad=0
posicion=0
print "El siguiente programa busca identificar la cadena de carácteres de mayor longitud,ingresada por el usuario."
print "Para detener el ciclo, no ingrese ninguna cadena...."

while True:    
    cadena= raw_input('Ingrese una cadena de carácteres: ')
    posicion=posicion+1
    #print 'Cant. carácteres: \t', len(cadena)
    #print 'Posicion: \t\t', posicion
    if (cantidad<len(cadena)):
        cantidad=len(cadena)
    if(cantidad>=len(cadena)):
        cantidad=cantidad
    if(len(cadena)==0):        
        break    
    
print 'La cadena de carácteres más larga, fue de: ', cantidad
print 'En la posición: ', posicion

       
