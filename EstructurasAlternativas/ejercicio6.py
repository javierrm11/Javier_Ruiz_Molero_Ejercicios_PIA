"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 6
Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().
"""

#pedir datos
num_1 = int(input("(1) Introduce un numero: "))
num_2 = int(input("(2) Introduce un numero: "))
num_3 = int(input("(3) Introduce un numero: "))

print()
num_mayor = num_1

#Calcular el numero mas alto
if num_2 > num_mayor:
    num_mayor = num_2

if num_3 > num_mayor:
    num_mayor = num_3

print(f"El numero mayor es: {num_mayor}")
