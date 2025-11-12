"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 3
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
 A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
 además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta
 el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

Para usar números aleatorios en Python: http://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html
"""
import random

# Variables
number_guess = random.randint(1, 100)
tries = 10

# Bucle para los intentos
while tries > 0:
    number = int(input("Adivine el numero del 1 al 100: "))
    # Comprobar si es mayor, menor o acertado
    if number > number_guess:
        print("El numero a adivinar es menor")
    elif number < number_guess:
        print("El numero a adivinar es mayor")
    else:
        print(f"Has adivinado el numero en {10 -tries} intentos")
        exit()
    if tries == 0:
        print("Te has quedado sin intentos")
        break
    tries -= 1
    print(f"Te quedan {tries} intentos")