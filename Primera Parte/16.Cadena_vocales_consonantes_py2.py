"""
Ejercicio16:Escribe un programa que reciba una cadena, y cuente el número de vocales y
consonantes que se encuentran en ella.
"""
# -*- coding: utf-8 -*-
cadena= raw_input('Ingrese una cadena de carácteres: ')
vocales=0
consonantes=0
espacio=0
i=0
ascii=0
while(i<len(cadena)):
    if (((cadena[i]=='a' or cadena[i]=='e')or (cadena[i]=='i' or cadena[i]=='o' ))or cadena[i]=='u'):
        vocales=vocales+1
    elif (((cadena[i]=='A'or cadena[i]=='E') or cadena[i]=='I')or (cadena[i]=='O'or cadena[i]=='U')):
        vocales=vocales+1
    elif (cadena[i]==' '):
        consonantes=consonantes
        espacio=espacio+1
    else:
        consonantes=consonantes+1
    i=i+1
    
print 'El numero de vocales es: ', vocales
print 'El numero de consonantes es: ', consonantes
print 'El numero de espacios es: ', espacio

       
