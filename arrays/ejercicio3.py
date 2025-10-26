"""
Ejercicio 3
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy.
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes.
Utiliza arrays auxiliares si es necesario.
"""
import numpy as np

numeros = np.random.randint(0,100,20)

numerosPares = numeros[numeros % 2 == 0]
numerosImpares = numeros[numeros % 2 != 0]

ordenado = np.concatenate((numerosPares, numerosImpares))

print(ordenado)
