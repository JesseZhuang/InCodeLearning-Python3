"""
This module learns about docstring and its recommended style.
https://www.python.org/dev/peps/pep-0257/
Docstring is the first statement in a module, function, class, or
method definition, which becomes the __doc__ special attribute of
that object.
Maximum line length inside docstring is 72 characters.
Triple double quotes are recommended.
Should contain usage message as a standalone script,
similar to when you type `ls --help` on linux command line.
"""

import sys


def oneline():
    """This is a one line docstring of a function."""

print(oneline())


def multiline():
    r"""
    First line should be a summary followed by a blank line.

    Subsequent lines should provide detailed information about
        the object. Indentations and formats are kept. Use r
        for backslashes \.
    """


# This comment will not show in help.
def unicode_docstring():
    u"""
    Unicode and raw formats cannot be used together.

    Use u to display Unicode strings 中文 \u4e2d\u6587
    inside docstrings.
    In python shell, use
        help(docstring.unicode_string) or
        docstring.unicode_string.__doc__
    to see the docstring.
    """


# comments above the function shows up
# in the help if no docstring available.
def empty_function():
    pass


# A real recommended example.
def my_complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex(0, 0)

print("raw form\n ", my_complex.__doc__)
print("splitted\n", my_complex.__doc__.splitlines())


def trim(docstring):
    """Process a docstring."""
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

print("processed\n ", trim(my_complex.__doc__))
