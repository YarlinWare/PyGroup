"""
Ejercicio17.Escribe un programa que reciba un conjunto de cadenas e imprima
cu�l es la de mayor longitud y en qu� posici�n se encuentra.
"""
# -*- coding: utf-8 -*-
cantidad=0
posicion=0
print "El siguiente programa busca identificar la cadena de car�cteres de mayor longitud,ingresada por el usuario."
print "Para detener el ciclo, no ingrese ninguna cadena...."

while True:    
    cadena= raw_input('Ingrese una cadena de car�cteres: ')
    posicion=posicion+1
    #print 'Cant. car�cteres: \t', len(cadena)
    #print 'Posicion: \t\t', posicion
    if (cantidad<len(cadena)):
        cantidad=len(cadena)
    if(cantidad>=len(cadena)):
        cantidad=cantidad
    if(len(cadena)==0):        
        break    
    
print 'La cadena de car�cteres m�s larga, fue de: ', cantidad
print 'En la posici�n: ', posicion

       
