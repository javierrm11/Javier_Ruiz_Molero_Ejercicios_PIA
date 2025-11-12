"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 5
Crea un programa que pida un número por teclado al usuario y diga si es primo.
En caso de que no se introduzca un número o que este sea menor que 2 se debe mostrar un mensaje de error.
"""

try:
    number = int(input("Introduce un número para saber si es primo: "))
    # Comprobar si es menor de 2
    if number < 2:
        print("Error: el número debe ser mayor o igual a 2.")
        exit()

    # Comprobación de número primo
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} es primo.")
    else:
        print(f"{number} no es primo.")

except ValueError:
    print("Error: debes introducir un número válido.")
