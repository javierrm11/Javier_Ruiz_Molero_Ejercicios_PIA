"""
Ejercicio 7
Crea un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización después de que se pida al usuario/a:

- Importe del préstamo.
- La tasa de interés anual.
- Y el plazo de pago en años.

Necesitaréis averiguar cómo se hace este cálculo (podéis preguntar a ChatGPT).
"""

print("Vamos a calcular la cuota de una hipoteca y su tabla de amortización")

# Pedir datos
importe_prestamo = float(input("Importe del préstamo (€): "))
tasa_interes_anual = float(input("Tasa de interés anual (%): "))
plazo_anios = int(input("Plazo de pago (años): "))

# Calcular valores base
tasa_mensual = tasa_interes_anual / 100 / 12
num_cuotas = plazo_anios * 12

# Calcular cuota mensual
cuota = importe_prestamo * (tasa_mensual * (1 + tasa_mensual)**num_cuotas) / ((1 + tasa_mensual)**num_cuotas - 1)

print(f"\n💰 Cuota mensual: {cuota:.2f} €")
print("\n📋 Tabla de amortización:\n")
print("Mes\tCuota\t\tInterés\t\tAmortización\tCapital pendiente")

capital_pendiente = importe_prestamo

for mes in range(1, num_cuotas + 1):
    interes = capital_pendiente * tasa_mensual
    amortizacion = cuota - interes
    capital_pendiente -= amortizacion

    print(f"{mes}\t{cuota:10.2f}\t{interes:10.2f}\t{amortizacion:13.2f}\t{capital_pendiente:15.2f}")

print("\nCálculo finalizado.")