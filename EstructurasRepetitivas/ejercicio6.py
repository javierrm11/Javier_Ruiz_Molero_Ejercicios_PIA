"""
Ejercicio 6
Crea un programa que muestre en pantalla los N primeros números primos.
El valor de N se pide por teclado al usuario/a.
"""

n = int(input("¿Cuántos números primos quieres ver?: "))

contador = 0
numero = 2
primos = []

while contador < n:
    #Comprobamos si el numero es primo
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(numero)
        contador += 1

    numero += 1

#Mostramos los resultados
for p in primos:
    print(f"{p} es primo.")
