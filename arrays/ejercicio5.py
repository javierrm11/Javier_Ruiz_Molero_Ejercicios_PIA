"""
Ejercicio 5
Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
"""
import random

# Generamos 20 números aleatorios entre 100 y 999
numeros = [random.randint(100, 999) for _ in range(20)]

# Creamos una "matriz" de 4x5 usando listas anidadas
matriz = [numeros[i*5:(i+1)*5] for i in range(4)]

# Calculamos sumas de filas y columnas
suma_filas = [sum(fila) for fila in matriz]
suma_columnas = [sum(matriz[fila][col] for fila in range(4)) for col in range(5)]
suma_total = sum(numeros)

# Mostramos la tabla estilo hoja de cálculo
print("Tabla con sumas parciales:")
for i in range(4):
    fila = " ".join(f"{num:4d}" for num in matriz[i])
    print(f"{fila} | {suma_filas[i]}")

# Mostramos la suma de columnas y la suma total
linea_columnas = " ".join(f"{num:4d}" for num in suma_columnas)
print("-" * 29)
print(f"{linea_columnas} | {suma_total}")
