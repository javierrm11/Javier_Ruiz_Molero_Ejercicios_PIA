"""
Date: 28/10/2025
@author: Javier Ruiz Molero

Ejercicio 6
Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
"""

import numpy as np

numbers = np.random.randint(100,999,20).reshape((4,5))

# Calculamos sumas de filas y columnas
sum_fills = numbers.sum(axis=1)
sum_columns = numbers.sum(axis=0)
sum_total = numbers.sum()

# Mostramos la tabla estilo hoja de cálculo
print("Tabla con sumas parciales:")
for i in range(numbers.shape[0]):
    fill = " ".join(f"{num:4d}" for num in numbers[i])
    print(f"{fill} | {sum_fills[i]}")

# Mostramos la suma de columnas
line_columns = " ".join(f"{num:4d}" for num in sum_columns)
print("-" * 29)
print(f"{line_columns} | {sum_total}")


