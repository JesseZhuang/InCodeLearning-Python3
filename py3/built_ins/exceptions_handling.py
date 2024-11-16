import sys  # used in Handling Unexpected Errors part


# https://docs.python.org/3/tutorial/errors.html?highlight=error%20handle

# Learning Objectives:
# 1. What are the basic exception handling methods
# 2. How to handle multiple exceptions at once
# 3. How to define your own exceptions
# 4. How to handle unexpected exceptions
# 5. How to use KeyboardInterrupt Exception (Optional)

# Exception Handling
# ==================


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(3, 0)
divide(4, 2)


"""
Example(s):
===========
>>> divide(1, 1)
('result is', 1)
executing finally clause

>>> divide(1, 0)
division by zero!
executing finally clause

>>> divide(1, "2")
Traceback (most recent call last):
  File "/home/map/PycharmProjects/test/test.py", line 25, in <module>
    divide(1, "2")
executing finally clause
  File "/home/map/PycharmProjects/test/test.py", line 7, in divide
    result = x / y
TypeError: unsupported operand type(s) for /: 'int' and 'str'
"""


# Mutiple Exceptions Handling
# ===========================


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print("operand type(s) not supported by /")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


"""
Example(s):
===========
>>> divide("1", "2")
operand type(s) not supported by /
executing finally clause
"""


def divide(x, y):
    try:
        result = x / y
    except (ZeroDivisionError, TypeError):
        print("division by zero or operand type(s) not supported by /")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


"""
Example(s):
===========
>>> divide(1,0)
division by zero or operand type(s) not supported by /
executing finally clause

>>> divide(1,'2')
division by zero or operand type(s) not supported by /
executing finally clause
"""


# User Defined Exception
# ======================


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidInputError(Error):
    """Exception raised for errors in the input."""

    def __init__(self, type_y):
        self.type_y = type_y


def divide(x, y):
    try:
        if type(y) not in (int, float, complex):
            raise InvalidInputError(type(y))
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except InvalidInputError as Inst:
        print("second input should not be {0}".format(Inst.type_y))
    except TypeError:
        print("operand type(s) not supported by /")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


"""
Example(s):
===========
>>> divide(1, "2")
second input should not be <type 'str'>
executing finally clause

>>> divide("1", 2)
operand type(s) not supported by /
executing finally clause
"""


# Handling Unexpected Errors
# ==========================


def divide(x, y):
    try:
        if type(y) not in (int, float, complex):
            raise InvalidInputError(type(y))
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except InvalidInputError as Inst:
        print("second input should not be {0}".format(Inst.type_y))
    except TypeError:
        print("operand type(s) not supported by /")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # Return information about the most recent exception caught
        raise
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# KeyboardInterrupt
# =================

# try Control-C or control-D
# use ps -ef | grep exception, kill <process-id> in linux

# while True:
#     try:
#         input("Please enter something: ")
#     except KeyboardInterrupt:
#         print("Program was interrupted from the keyboard.")
#     except:
#         print("Please enter something else: ")
