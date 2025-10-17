"""
Ejercicio 4
Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.
"""

#pedir monedas
dinero = int(input("Cuanto dinero tienes: "))

#variables de dinero
billete500 = 0
billete200 = 0
billete100 = 0
billete50 = 0
billete20 = 0
billete10 = 0
billete5 = 0
billete2 = 0
billete1 = 0

print()

# calcular monedas
if dinero > 500:
    billete500 = int(dinero / 500)
    dinero = dinero - billete500 * 500
if dinero > 200:
    billete200 = int(dinero / 200)
    dinero = dinero - billete200 * 200

if dinero > 100:
    billete100 = int(dinero / 100)
    dinero = dinero - billete100 * 100

if dinero > 50:
    billete50 = int(dinero / 50)
    dinero = dinero - billete50 * 50

if dinero > 20:
    billete20 = int(dinero / 20)
    dinero = dinero - billete20 * 20

if dinero > 10:
    billete10 = int(dinero / 10)
    dinero = dinero - billete10 * 10

if dinero > 5:
    billete5 = int(dinero / 5)
    dinero = dinero - billete5 * 5

if dinero > 2:
    billete2 = int(dinero / 2)
    dinero = dinero - billete2 * 2

if dinero >= 1:
    billete1 = int(dinero / 1)
    dinero = dinero - billete1 * 1

print(f"Tienes {billete500} billetes de 500€")
print(f"Tienes {billete200} billetes de 200€")
print(f"Tienes {billete100} billetes de 100€")
print(f"Tienes {billete50} billetes de 50€")
print(f"Tienes {billete20} billetes de 20€")
print(f"Tienes {billete10} billetes de 10€")
print(f"Tienes {billete5} billetes de 5€")
print(f"Tienes {billete2} billetes de 2€")
print(f"Tienes {billete1} billetes de 1€")





