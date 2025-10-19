"""
Ejercicio 1
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
"""

#pedir datos
numero1 = int(input("Introduce un numero inicial: "))
numero2 = int(input("Introduce un numero final: "))

# bucle del rango de los numeros
for numero in range(numero1, numero2+1):
    if numero % 2 == 0:
        print(numero)