"""
Ejercicio 7
Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max()..
"""
#pedir datos
numero1 = int(input("(1) Introduce un numero: "))
numero2 = int(input("(2) Introduce un numero: "))
numero3 = int(input("(3) Introduce un numero: "))
numero4 = int(input("(4) Introduce un numero: "))
numero5 = int(input("(5) Introduce un numero: "))



print()

#calcular si son todos iguales
if numero1 == numero2 == numero3 == numero4 == numero5:
    print("Son todos iguales")
    exit()

#Calcular el numero mas alto
if numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5:
    print(f"El numero 1 ({numero1}) es el mayor")
elif numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
    print(f"El numero 2 ({numero2}) es el mayor")
elif numero3 > numero4 and numero3 > numero5:
    print(f"El numero 3 ({numero3}) es el mayor")
elif numero4 > numero5:
    print(f"El numero 4 ({numero4}) es el mayor")
else:
    print(f"El numero 5 ({numero5}) es el mayor")

