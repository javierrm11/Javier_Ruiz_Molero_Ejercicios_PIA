"""
Date: 28/10/2025
@author: Javier Ruiz Molero

Ejercicio 5
Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
"""
import random

# Generamos 20 números aleatorios entre 100 y 999
numbers = [random.randint(100, 999) for _ in range(20)]

# Creamos una "matriz" de 4x5 usando listas anidadas
matrix = [numbers[i*5:(i+1)*5] for i in range(4)]

# Calculamos sumas de filas y columnas
sum_fills = [sum(fila) for fila in matrix]
sum_columns = [sum(matrix[fila][col] for fila in range(4)) for col in range(5)]
sum_total = sum(numbers)

# Mostramos la tabla estilo hoja de cálculo
print("Tabla con sumas parciales:")
for i in range(4):
    fill = " ".join(f"{num:4d}" for num in matrix[i])
    print(f"{fill} | {sum_fills[i]}")

# Mostramos la suma de columnas y la suma total
line_columns = " ".join(f"{num:4d}" for num in sum_columns)
print("-" * 29)
print(f"{line_columns} | {sum_total}")
