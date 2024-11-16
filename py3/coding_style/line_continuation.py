"""
Line continuations. Code across multiple lines in Python.
"""

# parentheses, brackets, braces preferred over backslashes
# note different from docstring, no \r \n
print('A very long line that cannot fit on one line that'
      'should be less than 80 characters. '
      'Also note this is different than docstring')

# backslash appropriate for other occasions, with statement
# Todo with statement across multiple lines
# with open('/path/to/some/file/you/want/to/read') as file_1, \
#      open('/path/to/some/file/being/written', 'w') as file_2:
#     file_2.write(file_1.read())
