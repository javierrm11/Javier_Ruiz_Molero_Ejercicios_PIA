"""
Ejercicio 2
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""

numeroImprimir = int(input("Ingrese los numero a imprimir: "))
numeros = []
mayores = 0
menores = 0
iguales = 0

# pedir numeros
while numeroImprimir > 0:
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
    numeroImprimir = numeroImprimir - 1

# recorrer numeros
for numero in numeros:
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print()
print(f"Mayores: {mayores}, Menores: {menores}, iguales: {iguales}")
