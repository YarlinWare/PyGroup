"""
Ejercicio 87: Escribir un programa que solicite al usuario una hora espec�fica en
formato hh:mm:ss y que la divida a trav�s del car�cter �:� para
posteriormente imprimirla a�adi�ndole un segundo.
"""
# -*- coding: utf-8 -*-

hora = raw_input("""
Ingrese una hora espec�fica en formato hh:mm:ss y
dividida a trav�s del car�cter �:� :
""")
datos = hora.split(':')
for x in datos:
    int(x)




if(datos[2]==59):
    datos[1]=00
if(datos[2]<=59):
    datos[2]=datos[2]+1        
if(datos[1]==59):
    datos[0]=datos[0]+1
if(datos[2]<=59):
    datos[1]=datos[1]+1    




 
print 'Hora:', datos[0], 'Minutos:', datos[1], 'Segundos:', datos[2]
#hora.reverse()

print hora

