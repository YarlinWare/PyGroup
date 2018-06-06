"""
Ejercicio 1: Crear un programa que solicite al usuario ingresar un número para
obtener un día de la semana. Si el número está entre 1 y 7 debe devolver
el correspondiente día (Ej: 1, “Lunes”). Si el número está fuera del rango,
debe mostrar un mensaje que diga “número incorrecto”. (Hacerlo con una
tupla y con una lista)
"""
# -*- coding: utf-8 -*-
semana = {1:"Lunes", 2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sábado",7:"Domingo"}
dia_semana = 0

while ((dia_semana <1) or (dia_semana >7)):
    dia_semana = int(raw_input('Ingrese un numero del 1 al 7: '))

print semana [dia_semana]

