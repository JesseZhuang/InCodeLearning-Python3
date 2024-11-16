import operator
import functools


def process_two_numbers(f, *args):
    return f(*args)

print(process_two_numbers(lambda x, y: x + y, 3, 4))
print(process_two_numbers(operator.add, 3, 4))

# xrange in python 2 becomes range in python 3
one_to_hundred = range(10)   # [0, 9]
print(functools.reduce(lambda x, y: x + y, one_to_hundred))


# http://www.secnetix.de/olli/Python/lambda_functions.hawk
def my_factorial(num):
    return functools.reduce(lambda x, y: x * y, range(1, num + 1), 1)

# list(generator) equivalent to [generator]
print([my_factorial(x) for x in range(1, 10)])
print(list(my_factorial(x) for x in range(1, 10)))
