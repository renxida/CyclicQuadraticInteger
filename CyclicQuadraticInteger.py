"""
@author Xida Ren

This module contains one class, the CyclicQuadraticInteger, used to represent elements
of Z_m [\sqrt{(rt)}]. Each element of these sets is of the form a + b*sqrt(rt) where a, b are drawn from Z_m.
"""
class CyclicQuadraticInteger:
    def __init__(self, a, b, m, rt=5):
        self.m = m
        self.rt = rt
        self.a, self.b = a%m, b%m
        self.__reduce__()

    def __reduce__(self):
        self.a = self.a%self.rt
        self.b = self.b%self.rt


    def __add__(self, other):
        if self.m != other.m or self.rt != other.rt:
            raise ValueError('attempting to add CyclicQuadraticInteger of different modulus/rt')
        a = self.a + other.a
        b = self.b + other.b
        return CyclicQuadraticInteger(a, b, self.m, self.rt)

    def __mul__(self, other):
        if self.m != other.m or self.rt != other.rt:
            raise ValueError('attempting to add CyclicQuadraticInteger of different modulus/rt')
        a = self.a * other.a + self.rt * self.b * other.b
        b = self.a * other.b + self.b * other.a
        a %= self.m
        b %= self.m
        return CyclicQuadraticInteger(a, b, self.m, self.rt)


    def __eq__(self, othr):
        if (self.m, self.rt, self.a, self.b) == \
           (othr.m, othr.rt, othr.a, othr.b):
            return True
        else:
            return False

    def __neg__(self):
        return self.new(-self.a, -self.b)

    def create(self, a, b):
        return CyclicQuadraticInteger(a%self.m, b%self.m, self.m, self.rt)

    def __str__(self):
        return '({a} + {b}√{rt} %% {m})'.format(a=self.a, b=self.b, rt=self.rt, m=self.m)

    def __repr__(self):
        return str(self)

    def all_elements(self):
        for i in range(self.rt):
            for j in range(self.rt):
                yield(i, j)

    def all_nonzero_elements(self):
        for i in range(1, self.rt):
            for j in range(1, self.rt):
                yield(i, j)

