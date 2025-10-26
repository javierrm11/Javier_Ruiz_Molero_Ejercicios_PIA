"""
Ejercicio 4
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.

Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar que funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Los números en Morse los puedes encontrar aquí.
"""

def convertirMorse(numero):
    morse_numeros = {
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

    numero = str(numero)
    morse = [morse_numeros[d] for d in numero]  # convierte cada dígito a su Morse
    return " ".join(morse)


# Programa principal
num = 213
resultado = convertirMorse(num)
print(f"El número {num} en Morse es: {resultado}")
