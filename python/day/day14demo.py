class Calc:
    def add(self, a, b):
        return a + b

    def subs(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def divi(self, a, b):
        return a / b


import unittest


class TestCalc(unittest.TestCase):

    def testadd(self):
        a = 1
        b = 2
        sum = 3
        c = Calc()
        s = c.add(a, b)

        self.assertEqual(sum, s)
