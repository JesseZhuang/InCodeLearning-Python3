"""Learn about the import statement."""

import sys
import os
import contextlib
from io import StringIO

save_stdout = sys.stdout
sys.stdout = StringIO()  # suppress output of import def_function
# note this fails pep8 on purpose
import def_function  # import a module
sys.stdout = save_stdout


@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = StringIO()
    yield
    sys.stdout = save_stdout

print(sys.path)  # maybe the empty string '' adds current path

# calls a function in the module imported
print(def_function.add_or_minus(10, 10))

# or insert(0, ...) to add at front
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'built_ins'))
print(sys.path)

# suppress stdout method 2
with nostdout():
    import built_in_functions

print(built_in_functions.Person("male", 34))
