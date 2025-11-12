"""
Date: 28/10/2025
@author: Javier Ruiz Molero

Ejercicio 3
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy.
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes.
Utiliza arrays auxiliares si es necesario.
"""
import numpy as np
# Creaccion de un array con numero aleatorios entre 0 y 100
numbers = np.random.randint(0,100,20)

# Guardamos los pares y impares en variables
numbers_even = numbers[numbers % 2 == 0]
numbers_odd = numbers[numbers % 2 != 0]

# Lo ordenamos poniendo primero los pares
ordinate = np.concatenate((numbers_even, numbers_odd))

print(ordinate)
