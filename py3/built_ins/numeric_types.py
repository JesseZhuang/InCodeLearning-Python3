import fractions
import math
# 1. Boolean


# class must be defined before use
class UserDefined1:
    def __bool__(self):
        return False


# class name should use camel cases like Java...
class UserDefined2:
    # class user_defined1:
    def __len__(self):
        return 0

# Any object can be tested for truth, following are considered false.
if (not (None or False or
         0 or 0j or 0.0 or  # pep8 aligning to opening parenthesis
         '' or () or [] or
         {} or
         UserDefined1() or UserDefined2())):
    print("hello all the False's, everything else is True.")

# legacy from python 2 True=1 False=0
logic_ops = {
    "True + True": True + True,
    "True - False": True - False,
    "True * 3": True * 3,
    # True/False division by zero Error
}

for k, v in logic_ops.items():
    print('  ', '{:<13}={:>6}'.format(k, v))


# comparison operators <, >, <=, >=,  ==, !=. In C, == and != has less
# precedence than the other 4. In python, all same, which has less precedence
# than arithmetic, bitwise, shifting operations.
# C precedence http://en.cppreference.com/w/c/language/operator_precedence
# Use parentheses when not sure.

A = 3
B = 6
C = 32

print(8, A == 3 < B)  # false in C, True in python
print(9, B != 8)
print(10, A > B)
print(11, A + B < C)

# test short circuit in C or Java
# if 1 < 2 and (a = 2) < 3:
# unfortunately python does not allow assignment in conditionals

# other functions that return boolean

D = 'abcdef'
print(12, 'a' in D)
print(13, 'h' not in D)
print(14, '' in D)
print(15, 'abcdef' is D)
# python caches small integers and small strings
# in python 2.7 3.5, [-5, 256] are cached
print(16, 'abcd' is not D)
# TODO: isinstance, issubclass
# TODO: string methods: tring methods, isslnum, isalpha, isdecimal, .etc

# "rich comparison"  special methods


def __eq__(one, other):
    # Todo: why not use == ?
    return not one < other and not other < one


def __ne__(one, other):
    # todo why not use != ?
    return one < other or other < one     # return not self == other


def __lt__(one, other):
    return one < other


def __le__(one, other):
    return not one > other


def __gt__(one, other):
    return other < one


def __ge__(one, other):
    return not one < other

p1 = 3
p2 = 4
print(21, p1.__lt__(p2))    # calls int.__lt__()
print(22, __lt__(p1, p2))   # calls __lt__() line 73 above
print(23, __le__(p1, p2))
print(24, __eq__(p1, p2))
print(25, __ne__(p1, p2))
print(26, __gt__(p1, p2))
print(27, __ge__(p1, p2))

# 2. Numbers

print("=====numbers=====")
print(type(1))
print(type(1.0))
print(type(1 + 1.0))   # coerce into float

# floating points accurate to 15 decimal places
print(float(2))
# int() truncates towards 0
print(int(-2.5))
# py2 has int/long, int limited by sys.maxint usually 2^32-1, PEP237
print(11 / 2)
# py2 / usually integer division unless from __future__ import division
# or python -Qnew foo.py todo find source/meaning of -Qnew
# py3 / means floating point division, pep238

# python directives __future__ pep236, pep263 coding in comment encoding
print(11 // 2)  # same in py2 py3
print(-11 // 2, 11 // -2)    # different in Java, C

print(fractions.Fraction(6, 4))
print(math.pi)
print(math.sin(math.pi / 2))
print(math.tan(math.pi / 4))   # python does not have infinite precision
