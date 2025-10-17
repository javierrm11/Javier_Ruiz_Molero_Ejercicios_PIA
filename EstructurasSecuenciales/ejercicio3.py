# 7. Realiza un programa que reciba una cantidad de minutos y muestre por
# pantalla a cuantas horas y minutos corresponde.

min = int(input("Ingrese cuantos minutos hay:"))
# Calcular horas y minutos
horas = min // 60
minutos = min % 60

print(f"{min} minutos equivalen a {horas} hora(s) y {minutos} minuto(s).")
