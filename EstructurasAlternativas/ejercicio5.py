"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 5
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
"""

day_week = int(input("Introduce el dia semana: (1 al 7): "))

print()

# Si el dia no es valido
if day_week < 1 or day_week > 7:
    print("El numero introducido es invalido")
    exit()

# Calcular el dia de la semana
if day_week == 1:
    print("Es lunes")
elif day_week == 2:
    print("Es martes")
elif day_week == 3:
    print("Es miercoles")
elif day_week == 4:
    print("Es jueves")
elif day_week == 5:
    print("Es viernes")
elif day_week == 6:
    print("Es sabado")
else:
    print("Es domingo")
