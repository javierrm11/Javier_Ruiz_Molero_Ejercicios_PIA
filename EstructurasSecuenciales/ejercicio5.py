# 12. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un programa que determine la hora de llegada a la ciudad B.

print("Calcular la hora de llegada del ciclista")

# hora de salida
hora_salida = input("A que hora sale de la ciudad a con la bici (HH:MM:SS): ")
# convertirlo en array
horas_split = hora_salida.split(":")
#guardar horas, minutos y segundos
horas = int(horas_split[0])
minutos = int(horas_split[1])
segundos = int(horas_split[2])

#duracion deñ viaje
tiempoViaje = int(input("Cuanto tarda de ir de ciudad a a ciudad b en segundos: "))

horasDuracion = tiempoViaje // 3600
minutosDuracion = (tiempoViaje % 3600) // 60
segundosDuracion = tiempoViaje % 60

horasLlegada = horas + horasDuracion
minutosLlegada = minutos + minutosDuracion
segundosLlegada = segundos + segundosDuracion

llegada = f"{horasLlegada}:{minutosLlegada}:{segundosLlegada}"

print(f"Llegada: {llegada}")
