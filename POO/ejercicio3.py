"""
Date: 03/11/2025
@author: Javier Ruiz Molero

Ejercicio 3
En Python podemos manejar fechas pero no nos gusta, vamos a crear una clase Date. Debe permitir:

- Crear fechas. Ejemplo: f = Date(17, 11, 2022)
- Ojo!!! Estas fechas son erróneas:
- Date(78, -45, 0)
- Date(31, 6, 2022)
- Date(29, 2, 2022)
- Las fechas se pueden comparar.
- A las fechas se le pueden sumar y restar días.
- Las fechas se pueden restar.
- Se debe poder averiguar el día de la semana de una fecha.
"""

class Date:
    def __init__(self, day, month, year):
        if year < 0 or month < 0 or day < 0:
            print("Date invalido")
            exit()
        if month < 1 or month > 12:
            print("Date invalido")
            exit()
        if month % 2 == 0 and day < 30 or month == 2 and day > 28:
            print("Date invalido")
            exit()
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month
    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f"({self.day}, {self.month}, {self.year})"

    # Comparaciones
    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.__year == other.year and self.__month == other.month and self.__day == other.day
    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.__year < other.year and self.__month < other.month and self.__day < other.day
    def __le__(self, other):
        return self == other or self < other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return not self < other
    def __ne__(self, other):
        return not self == other

    # operaciones
    def __add__(self, days):
        if not isinstance(days, int):
            return NotImplemented
        return Date(self.__year, self.__month, self.__day + days)
    def __sub__(self, other):
        if isinstance(other, Date):
            return Date(self.__year - other.__year, self.__month - other.__month, self.__day - other.__day)
        elif isinstance(other, int):
            return Date(self.__year, self.__month, self.__day - other)
        else:
            return NotImplemented


d1 = Date(17, 11, 2022)
d2 = Date(31, 6, 2022)

print(d1 == d2)
print(d1 > d2)
print(d1 >= d2)
print(d1 <= d2)
print(d1 != d2)
print(d1 + 10)
print(d1 - 10)
print(d1-d2)

