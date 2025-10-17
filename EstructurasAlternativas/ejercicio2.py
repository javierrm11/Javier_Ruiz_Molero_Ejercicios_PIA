
"""
Ejercicio 2
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
El programa debe determinar qué tipo de triángulo es:
- Si se cumple Pitágoras entonces es triángulo rectángulo.
- Si sólo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""

# Datos
lado1 = float(input("Ingrese el lado 1 del triángulo: "))
lado2 = float(input("Ingrese el lado 2 del triángulo: "))
lado3 = float(input("Ingrese el lado 3 del triángulo: "))
print()

# Triángulo equilátero
if lado1 == lado2 == lado3:
    print("Es un triángulo equilátero.")

# Triángulo isósceles
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triángulo isósceles.")

# Triángulo rectángulo (Pitágoras)
elif (
        round(lado1 ** 2, 5) == round(lado2 ** 2 + lado3 ** 2, 5) or
        round(lado2 ** 2, 5) == round(lado1 ** 2 + lado3 ** 2, 5) or
        round(lado3 ** 2, 5) == round(lado1 ** 2 + lado2 ** 2, 5)
):
    print("Es un triángulo rectángulo.")

# Triángulo escaleno
else:
    print("Es un triángulo escaleno.")
