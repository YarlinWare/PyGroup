"""
Ejercicio7:Escribe un programa que reciba dos números y establezca si el segundo es
mayor, menor o igual al cubo del primero.
"""
valor_uno = int(raw_input('Ingrese primer valor:\t'))
valor_dos = int(raw_input("Ingrese segundo valor:\t"))
cubo = valor_uno**3
if cubo > valor_dos:
    print valor_uno, " al cubo es igual a: ",cubo,"\n" ,valor_dos, " es menor al cubo de: ",valor_uno
elif cubo < valor_dos:
    print valor_uno, " al cubo es igual a: ",cubo,"\n" ,valor_dos, " es mayor al cubo de: ",valor_uno
else:
    print valor_uno, " al cubo es igual a: ",cubo,"\n" ,valor_dos, " es igual al cubo de: ",valor_uno


