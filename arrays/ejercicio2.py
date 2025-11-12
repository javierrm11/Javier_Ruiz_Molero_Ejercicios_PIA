"""
Date: 28/10/2025
@author: Javier Ruiz Molero

Ejercicio 2
Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""
import numpy as np

# Arrays con numpy
number = np.random.randint(1, 100, 100)
square = np.square(number)
cube = number ** 3


# Mostramos los resultados en tres columnas alineadas
print(f"{'Número':>8} {'Cuadrado':>10} {'Cubo':>10}")
print("-" * 32)
for i in range(len(number)):
    print(f"{number[i]:>8} {square[i]:>10} {cube[i]:>10}")
