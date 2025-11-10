"""
Date: 24/10/2025
@author: Javier Ruiz Molero

Ejercicio 7
Crea un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización después de que se pida al usuario/a:

- Importe del préstamo.
- La tasa de interés anual.
- Y el plazo de pago en años.

Necesitaréis averiguar cómo se hace este cálculo (podéis preguntar a ChatGPT).
"""

print("Vamos a calcular la cuota de una hipoteca y su tabla de amortización")

# Pedir datos
loan_amount = float(input("Importe del préstamo (€): "))
annual_interest_rate = float(input("Tasa de interés anual (%): "))
term_years = int(input("Plazo de pago (años): "))

# Calcular valores base
monthly_rate = annual_interest_rate / 100 / 12
number_of_installments = term_years * 12

# Calcular cuota mensual
installments = loan_amount * (monthly_rate * (1 + monthly_rate)**number_of_installments) / ((1 + monthly_rate)**number_of_installments - 1)

print(f"\n💰 Cuota mensual: {installments:.2f} €")
print("\n📋 Tabla de amortización:\n")
print("Mes\tCuota\t\tInterés\t\tAmortización\tCapital pendiente")

outstanding_capital = loan_amount

# recorrer los menes para las tasas
for mounth in range(1, number_of_installments + 1):
    interest = outstanding_capital * monthly_rate
    amortization = installments - interest
    outstanding_capital -= amortization

    print(f"{mounth}\t{installments:10.2f}\t{interest:10.2f}\t{amortization:13.2f}\t{outstanding_capital:15.2f}")

print("\nCálculo finalizado.")