"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 2
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
El programa debe determinar qué tipo de triángulo es:
- Si se cumple Pitágoras entonces es triángulo rectángulo.
- Si sólo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""

# Datos
side_1 = float(input("Ingrese el lado 1 del triángulo: "))
side_2 = float(input("Ingrese el lado 2 del triángulo: "))
side_3 = float(input("Ingrese el lado 3 del triángulo: "))
print()

# Triángulo equilátero
if side_1 == side_2 == side_3:
    print("Es un triángulo equilátero.")

# Triángulo isósceles
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Es un triángulo isósceles.")

# Triángulo rectángulo (Pitágoras)
elif (
        round(side_1 ** 2, 5) == round(side_2 ** 2 + side_3 ** 2, 5) or
        round(side_2 ** 2, 5) == round(side_1 ** 2 + side_3 ** 2, 5) or
        round(side_3 ** 2, 5) == round(side_1 ** 2 + side_2 ** 2, 5)
):
    print("Es un triángulo rectángulo.")

# Triángulo escaleno
else:
    print("Es un triángulo escaleno.")
