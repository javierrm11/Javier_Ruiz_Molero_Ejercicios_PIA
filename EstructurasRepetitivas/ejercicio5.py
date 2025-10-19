"""
Ejercicio 5
Crea un programa que pida un número por teclado al usuario y diga si es primo.
En caso de que no se introduzca un número o que este sea menor que 2 se debe mostrar un mensaje de error.
"""

try:
    numero = int(input("Introduce un número para saber si es primo: "))

    if numero < 2:
        print("Error: el número debe ser mayor o igual a 2.")
    else:
        # Comprobación de número primo
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"{numero} es primo.")
        else:
            print(f"{numero} no es primo.")

except ValueError:
    print("Error: debes introducir un número válido.")
