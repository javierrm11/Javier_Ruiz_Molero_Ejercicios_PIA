"""
Date: 20/10/2025
@author: Javier Ruiz Molero

Ejercicio 4
Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
"""

num = int(input("Ingresa un numero de dos cifras: "))

# Convertir a cadena para poder invertirlo
convert_num_string = str(num)
# Invertir el número usando slicing
num_reverse = convert_num_string[::-1]

#mostramos el numero invertido
print(f"El numero invertido: {num_reverse}")