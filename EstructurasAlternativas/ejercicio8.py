"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 8
Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen,
proporcione la calificación cualitativa correspondiente al número dado.

La calificación cualitativa será una de las siguientes:
- «Suspenso» (nota menor que 5),
- «Aprobado» (nota mayor o igual que 5, pero menor que 7),
- «Notable» (nota mayor o igual que 7, pero menor que 9),
- «Sobresaliente» (nota mayor o igual que 9, pero menor que 10),
- «Matrícula de Honor» (nota 10).
"""

qualification = float(input("Calificacion: "))

# Comprobar que sea un numero correcto
if qualification > 10 or qualification < 0:
    print("Calificacion no valida")
    exit()

# Calcular nota
if qualification == 10:
    print("Matrícula de Honor")
elif qualification >= 9:
    print("Sobresaliente")
elif qualification >= 7:
    print("Notable")
elif qualification >= 5:
    print("Aprobado")
else:
    print("Suspenso")