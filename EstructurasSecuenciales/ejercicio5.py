
"""
Date: 20/10/2025
@author: Javier Ruiz Molero

Ejercicio 5
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un programa que determine la hora de llegada a la ciudad B.
"""

print("Calcular la hora de llegada del ciclista")

# Hora de salida
hours_exit = input("A que hora sale de la ciudad a con la bici (HH:MM:SS): ")
# Convertirlo en array
hours_split = hours_exit.split(":")
# Guardar horas, minutos y segundos
hours = int(hours_split[0])
minutes = int(hours_split[1])
seconds = int(hours_split[2])

# Duracion del viaje
time_travel = int(input("Cuanto tarda de ir de ciudad a a ciudad b en segundos: "))

hours_duration = time_travel // 3600
minutes_duration = (time_travel % 3600) // 60
seconds_duration = time_travel % 60

hours_arrival = hours + hours_duration
minutes_arrival = minutes + minutes_duration
seconds_arrival = seconds + seconds_duration

arrival = f"{hours_arrival}:{minutes_arrival}:{seconds_arrival}"

print(f"Llegada: {arrival}")
