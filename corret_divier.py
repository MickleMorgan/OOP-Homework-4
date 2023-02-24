import math
from math import gcd


class Rational:
    """
    Class for operating with rational equations in python.

    """
    def __init__(self, a: int, b: int):
        """
        Init method with value check
        Attributes : a - nominator, b - denominator

        """
        if not isinstance(a, int):
            raise ValueError('a should be int')
        if not isinstance(b, int):
            raise ValueError('b should be int')
        if not b:
            raise ZeroDivisionError()

        self.__a = a
        self.__b = b

    def __add__(self, other):
        """
        Reassignment of the add method to work with rational

        """
        a = self.__a * other.__b + other.__a * self.__b
        b = self.__b * other.__b
        return Rational(a, b)

    def __sub__(self, other):
        """
        Reassignment of the sub method to work with rational

        """
        a = self.__a * other.__b - other.__a * self.__b
        b = self.__b * other.__b
        return Rational(a, b)

    def __mul__(self, other):
        """
        Reassignment of the mul method to work with rational

        """
        a = self.__a * other.__a
        b = self.__b * other.__b
        return Rational(a, b)

    def __truediv__(self, other):
        """
        Reassignment of the truediv method to work with rational

        """
        a = self.__a * other.__b
        b = self.__b * other.__a
        return Rational(a, b)

    def __str__(self):
        """
        Return string interpretation of the rational equation
        added method of simplifying by greatest common divider

        """
        sign = "-" if (self.__a * self.__b) < 0 else ""
        d = math.gcd(self.__a, self.__b)
        a, b = abs(self.__a), abs(self.__b)
        a //= d
        b //= d

        if a == b:
            return f'{sign}1'
        if b == 1:
            return f'{sign}{a}'
        if a > b:
            return f'{sign}{a // b} {a - a // b * b} / {b}'
        return f'{sign} {a} / {b}'


x1 = Rational(1, 3)
x2 = Rational(1, 2)
print(x1)
print(x2)
print(x1 + x2)
print(x1 - x2)
print(x1 / x2)
print(x1 * x2)
