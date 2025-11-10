"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 1
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
"""

#pedir datos
num_1 = int(input("Introduce un numero inicial: "))
num_2 = int(input("Introduce un numero final: "))

# bucle del rango de los numeros
for num in range(num_1, num_2+1):
    if num % 2 == 0:
        print(num)