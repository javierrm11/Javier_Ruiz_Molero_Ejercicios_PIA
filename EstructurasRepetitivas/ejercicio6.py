"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 6
Crea un programa que muestre en pantalla los N primeros números primos.
El valor de N se pide por teclado al usuario/a.
"""

n = int(input("¿Cuántos números primos quieres ver?: "))

counts = 0
number = 2
primes = []

# recorrer blucle hasta que count sea menor que el numero de primos que quiere el usuario
while counts < n:
    #Comprobamos si el numero es primo
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
        counts += 1

    number += 1

#Mostramos los resultados
for p in primes:
    print(f"{p} es primo.")
