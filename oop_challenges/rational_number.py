from math import gcd

class Rational:
    def __init__(self,p,q):
        self.p = p // gcd(p,q)
        if q != 0:
            self.q = q // gcd(p,q)
        else:
            raise Exception('Invalid Denominator')

    def __add__(self, other):
        num = (self.p * other.q) + (other.p * self.q)
        den = (self.q * other.q)
        return Rational(num, den)

    def __sub__(self, other):
        num = (self.p * other.q) - (other.p * self.q)
        den = (self.q * other.q)
        return Rational(num,den)

    def __mul__(self, other):
        num = self.p * other.p
        den = self.q * other.q
        return Rational(num,den)

    def __truediv__(self, other):
        num = self.p * other.q
        den = self.q * other.p
        return Rational(num,den)

    def __floordiv__(self, other):
        num = self.p * other.q
        den = self.q * other.p
        return Rational(num,den)

    def __eq__(self, other):
        return self.p == other.p and self.q == other.q

    def __ne__(self, other):
        return self.p != other.p or self.q != other.q

    def __lt__(self, other):
        return self.p * other.q < other.p * self.q

    def __gt__(self, other):
        return self.p * other.q > other.p * self.q

    def __le__(self, other):
        return self.p * other.q <= other.p * self.q

    def __ge__(self, other):
        return self.p * other.q >= other.p * self.q

    def __str__(self):
        if self.q == 1:
            return f'{self.p}'
        return f'{self.p}/{self.q}'

r1 = Rational(3,4)
r2 = Rational(5,6)
print('Addition:', r1 + r2)
print('Subtraction:', r1 - r2)
print('Multiplication:', r1 * r2)
print('Division:', r1 / r2)
print(f'{r1} < {r2}:', r1 < r2)