"""
Date: 03/11/2025
@author: Javier Ruiz Molero

Ejercicio 1
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable.

Debe permitir:
- Crear duraciones de tiempos. Ejemplo: t = Duration(10,20,56)
- Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
- Si no indico la hora, minuto o segundo estos valores son cero:
- Duration() --> (0, 0, 0)
- Duration(34) --> (34, 0, 0)
- Duration(34, 15) --> (34, 15, 0)
- Duration(34, 61) --> (35, 1, 0)
- Las duraciones de tiempo se pueden comparar.
- A las duraciones de tiempo les puedo sumar y restar segundos.
- Las duraciones de tiempo se pueden sumar y restar.
"""

class Duration:
    # metodo constructor
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        if hours < 0 or minutes < 0 or seconds < 0:
            print("Error! No se puede meter horas negatigas")
            exit()
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.__hours = total_seconds // 3600
        self.__minutes = total_seconds % 3600 // 60
        self.__seconds = total_seconds % 60

    # Metodos getters
    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    # Metodo para imprimir Duracion
    def __str__(self):
        return f"{self.__hours}, {self.__minutes}, {self.__seconds}"

    # Metodos para comparar
    def __eq__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        total_seconds_other = other.__hours * 3600 + other.__minutes * 60 + other.__seconds
        return total_seconds == total_seconds_other

    def __lt__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        total_seconds_other = other.__hours * 3600 + other.__minutes * 60 + other.__seconds
        return total_seconds < total_seconds_other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


    # Metodo para sumar duraciones o segundos
    def __add__(self, other):
        if isinstance(other, Duration):
            total_duracion = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
            total_duracion_other = other.__hours * 3600 + other.__minutes * 60 + other.__seconds

            total = total_duracion + total_duracion_other
        elif isinstance(other, int):
            total = self.__hours * 3600 + self.__minutes * 60 + self.__seconds + other
        else:
            return NotImplemented
        horasTotal = total // 3600
        minutesTotal = total % 3600 // 60
        secondsTotal = total % 60
        return Duration(horasTotal, minutesTotal, secondsTotal)

    # Metodo para restar duraciones o segundos
    def __sub__(self, other):
        if isinstance(other, Duration):
            total_duracion = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
            total_duracion_other = other.__hours * 3600 + other.__minutes * 60 + other.__seconds

            total = total_duracion - total_duracion_other
            if total < 0:
                total = 0
        elif isinstance(other, int):
            total = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
            total = total - other
        else:
            return NotImplemented
        hours_total = total//3600
        minutes_total = total%3600//60
        seconds_total = total%60
        return Duration(hours_total, minutes_total, seconds_total)


# Instanciar objetos y probar los metodos
t = Duration(11,11, 90)
t1 = Duration(11,11,90)
t2= Duration(3,0,0)
print(t)
print(t +t1)
print(t+ 2)
print(t-2)
print(t-t1)
print(t == t1)
print(t < t2)
print(t > t2)
print(t >= t2)
print(t2 >= t)


