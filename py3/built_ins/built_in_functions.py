import inspect

print("=====functions starting with a=====")
# abs() returns magnitude for complex number
numbers = [-1, -2.3, complex(3, 4)]
for n in numbers:
    print(abs(n))

print(all(numbers))  # true if all elements are true
print(any([0, None]))  # true if any element is true

print(ascii("中文Àabc"))  # use \x \U \u escapes
# \xhh hex value hh char
# \uxxxx 16 bit hex char
# \Uxxxxxxxx 32 bit hex value char
# https://docs.python.org/3/reference/lexical_analysis.html
print("\u4e2d\u6587\xc0abc")
print(repr("\u4e2d\u6587\xc0abc"))
print(repr("中文Àabc"), repr([1, 2]))  # string representation
# a class can define __repr__()


class Person:
    """
    Toy class representing a person with gender (male/female)
    and age (integer).
    """
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "[Person: " + self.gender + " " + str(self.age) + "]"

    def __str__(self):
        return self.gender + " " + str(self.age)

    def __index__(self):
        return self.age

Tom = Person("male", 34)
print(Tom)      # calls __str__
print((Tom,))   # computer in REPL calls __repr__
# calls __str__ of tuple then calls __repr__ on contents
# same result if __str__ not defined in Person
# stackoverflow 18393701
print(repr(Tom))

print("=====functions starting with b=====")
print(bin(10))
print(bin(Tom))  # use __index__ of object

# import built_in_functions at python shell will run this file
# help() intended for interactive use. Will also work in py file
# type quit to exit

# in python shell, from path.to.file.built_in_functions import Person
# replace / in path with . in python shell
# help(Person)  # this python file is a module

# class bool([x]), subclass of int, why class not function?
# C source https://github.com/python/cpython/blob/master/Include/boolobject.h
print("class bool()")
print(' ', bool() == bool(0 + 0j))

# class bytearray([source[,encoding[,errors]]]), when to use?
# binary sequence type, mutable sequence of bytes [0,255]
bytearray_types = {
    "string": ["bytearray", "utf-8"],
    # "string": ("bytearray", "utf-8"),
    "integer_size": 10,
    # object conforming buffer interface to do
    "iterable": [1, 2, 3, 4]
}
print("class bytearrays")
for k, v in bytearray_types.items():
    if k == "string":
        print(' ', k, bytearray(*v))  # unpack args from tuple or list
    else:
        print(' ', k, bytearray(v))

print("class bytes")
# class bytes([source[, encoding[, errors]]]), immutable bytearray
print("  with bytes literal", bytes(rb'34\t'))
print("  with iterable", bytes([3, 4, 92, 116]))
print(' ', bytes(rb'34\t') == bytes([3, 4, 92, 116]))        # False
print(' ', bytes(b'\x03\x04\\t') == bytes([3, 4, 92, 116]))  # True
print(' ', bytes(b'\x33\x34\\t') == bytes(rb'34\t'))         # True

print("=====functions starting with c=====")
print("callable() since 3.2")


def test():
    print("hello from test")
print(' ', callable(test))
print(' ', callable(Tom))
# instances are callable if class has __call__() method
print(' ', callable(Person))  # classes are callable, return instance

print("chr() dec int to character, valid 0 - 0x10FFFF")
print(' ', chr(97))
print(' ', ord('a'))
# check wiki code point, 17 code planes, 17x2^16 = 1,114,112

print("=====functions starting with i=====")
# for CPython address of object in memory
print(id(1))
# 10105824 in win10ubuntu,  140474825689632 virtualbox-ubuntu
print(id([1, 2, 3]))
# 140076387922824 in win10ubuntu, 140587582331208 in virtualbox-ubuntu
list1 = [10, 11, 12]
print(id(list1))
# 140587582331208, interesting that address did not change
print(hex(id(list1)))
# 0x7fdd18e79948 64 bit ubuntu

print("=====functions starting with l=====")
# class list([iterable]) rather than being a function, list is a type
print(list({1:2, 3:6}))    # interesting, just took the keys out

print("=====functions starting with r=====")
# class range(stop), range(start, stop[,step])
print(*range(5))
# print(range(5.0, 10.0, 0.5)) TypeError
print(*range(5, 15))
print(*range(5, 15, 2))

print("=====functions starting with t=====")
# type(object) returns a type object
print(type(1))
# print(1.__class__) confuse python parser
print(1 .__class__, (1).__class__)
# isinstance() recommended for testing type taking subclass into account
print(type(1) == object)
print(isinstance(1, object))
# type(name, bases, dict)

# class tuple([iterable])
print(tuple({1:2, 3:6}))


class test:
    a = 1

test_object = test()
print(type(test_object))
print(type('test', (object,), dict(a=1)))
