"""
Ejercicio 5
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
"""

diaSemana = int(input("Introduce el dia semana: (1 al 7): "))

print()

# si el dia no es valido
if diaSemana < 1 or diaSemana > 7:
    print("El numero introducido es invalido")
    exit()

# calcular el dia de la semana
if diaSemana == 1:
    print("Es lunes")
elif diaSemana == 2:
    print("Es martes")
elif diaSemana == 3:
    print("Es miercoles")
elif diaSemana == 4:
    print("Es jueves")
elif diaSemana == 5:
    print("Es viernes")
elif diaSemana == 6:
    print("Es sabado")
else:
    print("Es domingo")
