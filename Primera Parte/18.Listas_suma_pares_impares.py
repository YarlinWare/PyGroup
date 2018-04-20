# -*- coding: utf-8 -*-

i=0
lista = []
cadena=raw_input("Dame 5 valores separados por comas: ")
pares=0
impares=0

print lista[cadena]
while(i<lista[i]):
    if ((cadena[i]%2)==0):
        pares=pares+cadena[i]
    else:
        impares=impares+cadena[i]
i=i+1

'''while(i<len(cadena)):
    if (cadena[i]==','):
        lista[i]=cadena[i]
    else:
        lista[i]=int(cadena[i])
        if ((cadena[i]%2)==0):
            pares=pares+cadena[i]
        elif(cadena[i]==','):
            pares=pares
        else:
            impares=impares+cadena[i]
i=i+1'''
    
    

print 'La suma de los números pares es: ', pares
print 'La suma de los números impares es: ', impares
