"""
Date: 20/10/2025
@author: Javier Ruiz Molero

Ejercicio 3
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
"""

min = int(input("Ingrese cuantos minutos hay:"))

# Calcular horas y minutos
hours = min//60
minutes = min%60

print(f"{min} minutos equivalen a {hours} hora(s) y {minutes} minuto(s).")
