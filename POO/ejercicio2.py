"""
Date: 03/11/2025
@author: Javier Ruiz Molero

Ejercicio 2
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

- Crear fracciones indicando numerador y denominador. Ejemplo: f = Fraction(2, 3)
- Ojo!!! No se puede tener un denominador cero.
- Las fracciones pueden operar entre sí.
- Sumar, multiplicar, dividir, restar.
- Ojo!!! esto se puede hacer: f + 1, 5 * f
- Las fracciones se pueden comparar.
- ==, <, <=, >, >=, !=
- Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
- Ojo!!! esto se puede hacer 1 < 1/2
"""
import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator no puede ser cero")
        # Simplificar la fracción
        gcd = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    @property
    def numerator(self):
        return self.__numerator
    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, numerator):
        # Simplificar la fracción
        gcd = math.gcd(numerator, self.__denominator)
        self.__numerator = numerator // gcd
        self.__denominator = self.__denominator // gcd

    @denominator.setter
    def denominator(self, denominator):
        if denominator == 0:
            print("No se puede tener un denominador cero.")
            exit()
        # Simplificar la fracción
        gcd = math.gcd(self.__numerator, denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = denominator // gcd

    # Metodo para imprimir Fracciones
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.__numerator + other, self.__denominator)
        elif not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.__numerator + other.__numerator, self.__denominator + other.__denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            return Fraction(self.__numerator - other, self.__denominator)
        elif not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.__numerator, self.__denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.__numerator * other, self.__denominator)
        elif not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.__numerator * other, self.__denominator)
        elif not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)
    def __eq__(self, other):
        if isinstance(other, int):
            return self.__numerator == other and self.__denominator == other
        elif isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.__numerator < other and self.__denominator < other
        elif isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator
    def __le__(self, other):
        return self == other or self < other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return not self < other
    def __ne__(self, other):
        return not self == other

f = Fraction(2,4)
f1 = Fraction(1,2)
print(f)
print(f +2)
print(f)
print(f+f1)
print(f==f1)
print(f>f1)
print(f>=f1)
print(f<f1)
print(f!=f1)
print(f==10)
print(f<10)
f.numerator = 4
print(f)

