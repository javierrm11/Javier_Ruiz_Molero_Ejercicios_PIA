"""
Ejercicio 4
Escribe un programa que pida el limite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.
"""

#variables
limiteinferior = int(input("Indique el limite inferior: "))
limitesuperior = int(input("Indique el limite superior: "))
numeros = []

#comprobar si el inferior es mayor que el superior
while limiteinferior > limitesuperior:
    limiteinferior = int(input("Indique el limite inferior: "))
    limitesuperior = int(input("Indique el limite superior: "))

# pedir numeros hasta que ponga 0
while True:
    numero = int(input("Introduce un numero: "))
    if (numero == 0):
        break
    numeros.append(numero)

# suma dentro del intervalo
numeros_dentro = [n for n in numeros if limiteinferior <= n <= limitesuperior]
print(f"La suma de los números dentro del intervalo es {sum(numeros_dentro)}")

# total numeros fuera intervalo
fuera = [n for n in numeros if n < limiteinferior or n > limitesuperior]
print(f"Hay {len(fuera)} números fuera del intervalo")

# informar si ha introducido numeros igual al intervalo
iguales = [n for n in numeros if n == limiteinferior or n == limitesuperior]
print(f"Hay {len(iguales)} números iguales al intervalo")

