"""
Date: 20/10/2025
@author: Javier Ruiz Molero

Ejercicio 2
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""
import math

# Pedir los catetos al usuario
leg_a = float(input("Ingresa la longitud del cateto A: "))
leg_b = float(input("Ingresa la longitud del cateto B: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hypotenuse = math.sqrt(leg_a*2 + leg_b*2)

# Mostrar el resultado
print(f"La hipotenusa del triángulo es: {hypotenuse:.2f}")
