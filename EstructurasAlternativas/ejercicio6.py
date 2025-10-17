"""
Ejercicio 6
Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().
"""

#pedir datos
numero1 = int(input("(1) Introduce un numero: "))
numero2 = int(input("(2) Introduce un numero: "))
numero3 = int(input("(3) Introduce un numero: "))

print()

#Calcular el numero mas alto
if numero1 > numero2 and numero1 > numero3:
    print(f"El numero 1 ({numero1}) es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero 2 ({numero2}) es el mayor")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero 3 ({numero3}) es el mayor")
else:
    print("Los numeros son iguales")
