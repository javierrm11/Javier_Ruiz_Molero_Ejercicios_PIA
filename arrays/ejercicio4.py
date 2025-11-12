"""
Date: 28/10/2025
@author: Javier Ruiz Molero

Ejercicio 4
Escribe un programa que lea 5 números por teclado y que los almacene en una lista.
Rota los elementos de esa lista, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc.
El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.
"""
import numpy as np

list = np.array([])

# Recogemos los 5 numero por teclado y los añadimos a la lista
for i in range(5):
    number = int(input("Introduce un numero: "))
    list = np.append(list, number)

# Rotamos la lista con numpy
list_rotate = np.roll(list, 1) # mueve una posicion a la derecha y si es el ultimo lo pasa al primero

print(list_rotate)