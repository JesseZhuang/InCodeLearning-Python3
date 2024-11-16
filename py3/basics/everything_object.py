# Everything in python is an object: assigned to var, passed to function
# Functions are first class citizens. Python first class everything.
# https://en.wikipedia.org/wiki/First-class_function


def i_am_an_object(param):
    return param


# higher order functions, function as argument
def square(num):
    return num * num


def cubic(square, num):
    return num * square(num)


def second_element(a_tuple):
    return a_tuple[1]
