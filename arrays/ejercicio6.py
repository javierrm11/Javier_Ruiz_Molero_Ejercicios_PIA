"""
Ejercicio 6
Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
"""

import numpy as np

numeros = np.random.randint(100,999,20).reshape((4,5))

# Calculamos sumas de filas y columnas
suma_filas = numeros.sum(axis=1)
suma_columnas = numeros.sum(axis=0)
suma_total = numeros.sum()

# Mostramos la tabla estilo hoja de cálculo
print("Tabla con sumas parciales:")
for i in range(numeros.shape[0]):
    fila = " ".join(f"{num:4d}" for num in numeros[i])
    print(f"{fila} | {suma_filas[i]}")

# Mostramos la suma de columnas
linea_columnas = " ".join(f"{num:4d}" for num in suma_columnas)
print("-" * 29)
print(f"{linea_columnas} | {suma_total}")


