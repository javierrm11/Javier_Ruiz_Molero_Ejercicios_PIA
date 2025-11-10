"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 3
Escribir un programa que lea un año indicar si es bisiesto (un año es bisiesto si es un número divisible por 4,
pero no si es divisible por 100, excepto que también sea divisible por 400).
"""

year = int(input("Ingresa el anio para saber si es bisiesto: "))
print()

#Comprobar si es bisiesto
if year % 4 == 0 and year % 100 != 0:
    print("Bisiesto")
else:
    print("No es bisiesto")
