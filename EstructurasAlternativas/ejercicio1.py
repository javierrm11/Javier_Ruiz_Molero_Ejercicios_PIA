"""
Ejercicio 1
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
"""

persona1 = int(input("Ingresa la edad de la persona 1: "))
persona2 = int(input("Ingresa la edad de la persona 2: "))
print()

# Comprobar si tienen la misma edad
if persona1 == persona2:
    print("La persona 1 y la persona 2 tienen la misma edad.")
    exit()

#Comprobamos quien es mayor
if(persona1 > persona2):
    print("La persona 1 es mayor que la persona 2.")
else:
    print("La persona 2 es mayor que la persona 1.")