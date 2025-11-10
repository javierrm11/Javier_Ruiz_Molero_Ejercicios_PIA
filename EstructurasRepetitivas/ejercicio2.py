"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 2
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""

number_imprint = int(input("Ingrese los numero a imprimir: "))
numbers = []
older = 0
younger = 0
equal = 0

# pedir numeros
while number_imprint > 0:
    number = int(input("Ingrese un numero: "))
    numbers.append(number)
    number_imprint = number_imprint - 1

# recorrer numeros
for number in numbers:
    if number > 0:
        older += 1
    elif number < 0:
        younger += 1
    else:
        equal += 1

print()
print(f"Mayores: {older}, Menores: {younger}, iguales: {equal}")
