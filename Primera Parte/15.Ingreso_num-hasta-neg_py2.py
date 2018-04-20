"""
Ejercicio15.Escribe un programa que reciba números enteros hasta que le llegue un número
negativo, después de lo cual termine el proceso.
"""

salir = 1
while (salir == 1):
    numero = int(raw_input('Ingrese numero: '))
    if(numero>=0):
        #print "Numero real mayor o igual que cero"
        salir = 1
    else:
        #print "Numero real menor que cero"
        salir = 0
        
       
