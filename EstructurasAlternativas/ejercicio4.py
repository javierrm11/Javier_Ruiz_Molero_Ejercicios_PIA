"""
Date: 22/10/2025
@author: Javier Ruiz Molero

Ejercicio 4
Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.
"""

#pedir monedas
money = int(input("Cuanto dinero tienes: "))

#variables de dinero
ticket_500 = 0
ticket_200 = 0
ticket_100 = 0
ticket_50 = 0
ticket_20 = 0
ticket_10 = 0
ticket_5 = 0
ticket_2 = 0
ticket_1 = 0

print()

# calcular monedas
if money > 500:
    ticket_500 = int(money / 500)
    money = money - ticket_500 * 500
if money > 200:
    ticket_200 = int(money / 200)
    money = money - ticket_200 * 200

if money > 100:
    ticket_100 = int(money / 100)
    money = money - ticket_100 * 100

if money > 50:
    ticket_50 = int(money / 50)
    money = money - ticket_50 * 50

if money > 20:
    ticket_20 = int(money / 20)
    money = money - ticket_20 * 20

if money > 10:
    ticket_10 = int(money / 10)
    money = money - ticket_10 * 10

if money > 5:
    ticket_5 = int(money / 5)
    money = money - ticket_5 * 5

if money > 2:
    ticket_2 = int(money / 2)
    money = money - ticket_2 * 2

if money >= 1:
    ticket_1 = int(money / 1)
    money = money - ticket_1 * 1

print(f"Tienes {ticket_500} billetes de 500€")
print(f"Tienes {ticket_200} billetes de 200€")
print(f"Tienes {ticket_100} billetes de 100€")
print(f"Tienes {ticket_50} billetes de 50€")
print(f"Tienes {ticket_20} billetes de 20€")
print(f"Tienes {ticket_10} billetes de 10€")
print(f"Tienes {ticket_5} billetes de 5€")
print(f"Tienes {ticket_2} billetes de 2€")
print(f"Tienes {ticket_1} billetes de 1€")





