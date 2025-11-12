"""
Date: 30/10/2025
@author: Javier Ruiz Molero

Ejercicio 4
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.

Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar que funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Los números en Morse los puedes encontrar aquí.
"""

def converter_morse(number):
    morse_numbers = {
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }

    number = str(number)
    morse = [morse_numbers[d] for d in number]  # Convierte cada dígito a su Morse
    return " ".join(morse)


# Programa principal
num = 213
result = converter_morse(num)
print(f"El número {num} en Morse es: {result}")
