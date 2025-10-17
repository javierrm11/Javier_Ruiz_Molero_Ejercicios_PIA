"""
Ejercicio 3
Escribir un programa que lea un año indicar si es bisiesto (un año es bisiesto si es un número divisible por 4,
pero no si es divisible por 100, excepto que también sea divisible por 400).
"""

anio = int(input("Ingresa el anio para saber si es bisiesto: "))
print()

#Comprobar si es bisiesto
if (anio % 4 == 0) and (anio % 100 != 0):
    print("Bisiesto")
else:
    print("No es bisiesto")
