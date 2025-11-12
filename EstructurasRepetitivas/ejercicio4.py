"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 4
Escribe un programa que pida el limite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.
"""

# Variables
lower_limit = int(input("Indique el limite inferior: "))
upper_limit = int(input("Indique el limite superior: "))
numbers = []

# Comprobar si el inferior es mayor que el superior
while lower_limit > upper_limit:
    lower_limit = int(input("Indique el limite inferior: "))
    upper_limit = int(input("Indique el limite superior: "))

# Pedir numeros hasta que ponga 0
while True:
    number = int(input("Introduce un numero: "))
    if number == 0:
        break
    numbers.append(number)

# Suma dentro del intervalo
numbers_inside = [n for n in numbers if lower_limit <= n <= upper_limit]
print(f"La suma de los números dentro del intervalo es {sum(numbers_inside)}")

# Total numeros fuera intervalo
outside = [n for n in numbers if n < lower_limit or n > upper_limit]
print(f"Hay {len(outside)} números fuera del intervalo")

# Informar si ha introducido numeros igual al intervalo
equeals = [n for n in numbers if n == lower_limit or n == upper_limit]
print(f"Hay {len(equeals)} números iguales al intervalo")

