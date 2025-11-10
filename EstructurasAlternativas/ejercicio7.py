"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 7
Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max()..
"""
#pedir datos
num_1 = int(input("(1) Introduce un numero: "))
num_2 = int(input("(2) Introduce un numero: "))
num_3 = int(input("(3) Introduce un numero: "))
num_4 = int(input("(4) Introduce un numero: "))
num_5 = int(input("(5) Introduce un numero: "))



print()

#calcular si son todos iguales
if num_1 == num_2 == num_3 == num_4 == num_5:
    print("Son todos iguales")
    exit()

num_mayor = num_1

#Calcular el numero mas alto
if num_2 > num_mayor:
    num_mayor = num_2

if num_3 > num_mayor:
    num_mayor = num_3

if num_4 > num_mayor:
    num_mayor = num_4

if num_5 > num_mayor:
    num_mayor = num_5

print(f"El numero mayor es: {num_mayor}")

