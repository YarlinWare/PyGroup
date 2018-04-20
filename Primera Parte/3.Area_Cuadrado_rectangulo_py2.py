
import math
import decimal
from decimal import Decimal, getcontext
"""
Ejercicio3:Escribe un programa que reciba un lado de un cuadrado y muestre su área, su
perímetro y su diagonal. Piensa: ¿Y si tuviéramos que hacer lo mismo con un
rectángulo?, modifica el programa anterior para que pueda aceptar también dicha
figura.
"""
# -*- coding: utf-8 -*-
opcion = int(raw_input('Ingrese segun corresponda\n 1.Cuadrado\n 2.Rectangulo\n Opcion:'))

if (opcion == 1):
    print "-----****-----\t CUADRADO \t-----****-----"
    lado = int(raw_input('Ingrese tamaño de un lado del cuadrado: '))
    
    if(lado<0):
        lado = lado * -1
        print "Al parecer haz ingresado un valor negativo por error,\n tomaremos el valor como positivo: ",lado
        
    area = lado * lado
    perimetro = 4 * lado
    diagonal = Decimal(math.sqrt((lado**2)+(lado**2)))    
    print "Area:     \t",area
    print "Perimetro: \t",perimetro
    print "Diagonal: \t",diagonal

    
elif (opcion == 2):
    
    print "-----****-----\t RECTANGULO \t-----****-----"
    base = int(raw_input('Ingrese la base del rectangulo:\t'))
    altura = int(raw_input("Ingrese la altura del rectangulo:\t"))
    
    if(base<0):
        base = base * -1
        print "Al parecer haz ingresado una base negativa por error,\n tomaremos el valor como positivo: ",base
    if(altura<0):
        altura = altura * -1
        print "Al parecer haz ingresado una altura negativa por error,\n tomaremos el valor como positivo: ",altura
        
    area = base * altura
    perimetro = (2 * base) + (2 * altura)
    diagonal = Decimal(math.sqrt((base**2)+(altura**2)))
    print "Area:      \t",area
    print "Perimetro: \t",perimetro
    print "Diagonal: \t",diagonal
    
    if (base == altura):
        print "Haz ingresado las dimensiones de un cuadrado (-_-)..."
else:
    print "Numero ingresado invalido...\n"
    

