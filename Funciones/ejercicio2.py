"""
Ejercicio 2
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función is_palindromic() resulta trivial teniendo reverse() y la función next_prime() también es muy fácil de implementar teniendo is_prime().

Está prohibido usar funciones de conversn del número a una cadena.

- is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
- is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
- next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
- digits: devuelve el número de dígitos de un número entero.
- reverse: le da la vuelta a un número.
- digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
- digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
- remove_behind: le quita a un número n dígitos por detrás (por la derecha).
- remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
- paste_behind: añade un dígito a un número por detrás.
- paste_ahead: añade un dígito a un número por delante.
- piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
- concatenate: pega dos números para formar uno.
Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.
"""
from operator import invert

from ejercicios.EstructurasRepetitivas.ejercicio6 import es_primo

# Función: is_palindromic
def is_palindromic(numero):
    return numero == reverse(numero)


# Función: is_prime
def is_prime(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Función: next_prime
def next_prime(numero):
    numero += 1
    while not is_prime(numero):
        numero += 1
    return numero


# Función: digits
def digits(numero):
    numero = abs(numero)
    if numero == 0:
        return 1
    contador = 0
    while numero > 0:
        numero //= 10
        contador += 1
    return contador


# Función: reverse
def reverse(numero):
    invertido = 0
    negativo = numero < 0
    numero = abs(numero)
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero //= 10
    return -invertido if negativo else invertido


# Función: digit_n
def digit_n(numero, n):
    longitud = digits(numero)
    return (numero // 10 ** (longitud - n - 1)) % 10


# Función: digit_position
def digit_position(numero, digito):
    longitud = digits(numero)
    for i in range(longitud):
        if digit_n(numero, i) == digito:
            return i
    return -1


# Función: remove_behind
def remove_behind(numero, n):
    return numero // (10 ** n)


# Función: remove_ahead
def remove_ahead(numero, n):
    return numero % (10 ** (digits(numero) - n))


# Función: paste_behind
def paste_behind(numero, digito):
    return numero * 10 + digito


# Función: paste_ahead
def paste_ahead(numero, digito):
    return digito * (10 ** digits(numero)) + numero


# Función: piece_of_number
def piece_of_number(numero, inicio, fin):
    # Extrae los dígitos entre inicio y fin (inclusive)
    longitud = digits(numero)
    numero = remove_behind(numero, longitud - fin - 1)
    numero = remove_ahead(numero, inicio)
    return numero


# Función: concatenate
def concatenate(num1, num2):
    return num1 * (10 ** digits(num2)) + num2


# -------------------------------
# PRUEBAS DE LAS FUNCIONES
# -------------------------------

print("is_palindromic(12321):", is_palindromic(12321))
print("is_prime(7):", is_prime(7))
print("next_prime(10):", next_prime(10))
print("digits(12345):", digits(12345))
print("reverse(1234):", reverse(1234))
print("digit_n(98765, 2):", digit_n(98765, 2))
print("digit_position(98765, 7):", digit_position(98765, 7))
print("remove_behind(98765, 2):", remove_behind(98765, 2))
print("remove_ahead(98765, 2):", remove_ahead(98765, 2))
print("paste_behind(123, 4):", paste_behind(123, 4))
print("paste_ahead(123, 4):", paste_ahead(123, 4))
print("piece_of_number(987654, 1, 3):", piece_of_number(987654, 1, 3))
print("concatenate(123, 456):", concatenate(123, 456))
