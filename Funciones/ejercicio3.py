"""
Date: 30/10/2025
@author: Javier Ruiz Molero

Ejercicio 3
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por pantalla,
 solo se debe usar print desde el programa principal.
"""

def conversational(number):
    output = ""
    number = str(number)
    # Recorrer los numeros
    for n in number:
        output += "|" * int(n) + "-"

    return output[0:-1]

print(conversational(470213))
print(conversational(1))
