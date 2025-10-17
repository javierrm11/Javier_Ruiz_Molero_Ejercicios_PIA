"""
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

calificacion = float(input("Calificacion: "))

#Comprobar que sea un numero correcto
if calificacion > 10 or calificacion < 0:
    print("Calificacion no valida")
    exit()

#Calcular nota
if calificacion == 10:
    print("Matrícula de Honor")
elif calificacion >= 9:
    print("Sobresaliente")
elif calificacion >= 7:
    print("Notable")
elif calificacion >= 5:
    print("Aprobado")
else:
    print("Suspenso")