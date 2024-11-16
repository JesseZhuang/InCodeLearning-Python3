"""There are several special methods which are not called directly,
but called by other syntax of the class or the instance of the class,
such as __init__, __next__, __iter__ etc
The class can act like sequence, dict, function, iterator, or number.
http://www.python-course.eu/python3_magic_methods.php
"""


class Length:

    __metric = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344
    }

    def __init__(self, value, unit='m'):
        self.value = value
        self.unit = unit

    def converse2meters(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        l = self.converse2meters() + other.converse2meters()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __str__(self):
        return str(self.converse2meters())

    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"

if __name__ == "__main__":
    x = Length(4)
    print(x)
    a = x.__init__(3)
    print(a)
    y = eval(repr(x))
    print(y)
    print(x)
    print(a)

    z = Length(4.5, "yd") + Length(1)
    print(repr(z))
    print(z)

    L = Length
    print(L(2.56, "m") + L(3, "yd") + L(7.8, "in") + L(7.03, "cm"))

# The difference between __init__ and __new__
# __init__ is always called after __new__
# http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init
# if not familiar with __new__, not use it (Suggestion)
