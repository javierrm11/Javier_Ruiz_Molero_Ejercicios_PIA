# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math

# Pedir los catetos al usuario
cateto_a = float(input("Ingresa la longitud del cateto A: "))
cateto_b = float(input("Ingresa la longitud del cateto B: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto_a*2 + cateto_b*2)

# Mostrar el resultado
print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")
