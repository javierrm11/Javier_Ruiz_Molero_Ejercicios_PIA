"""
Date: 28/10/2025
@author: Javier Ruiz Molero

Ejercicio 1
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube.
 Carga las lista number con valores aleatorios entre 0 y 100.
En la lista square se deben almacenar los cuadrados de los valores que hay en number.
 En la lista cube se deben almacenar los cubos de los valores que hay en number.
A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.
"""
import random

number = []
square = []
cube = []

#recorrer 20 veces un ciclo
for i in range(20):
    n = random.randint(0,100)
    number.append(n)

    #calcular el cuadrado y el cubo
    square.append(n**2)
    cube.append(n**3)


# Mostramos los resultados en tres columnas alineadas
print(f"{'Número':>8} {'Cuadrado':>10} {'Cubo':>10}")
print("-" * 32)

for i in range(20):
    print(f"{number[i]:>8} {square[i]:>10} {cube[i]:>10}")