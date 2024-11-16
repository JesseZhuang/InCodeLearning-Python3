import sys
import decimal
from fractions import Fraction

# dictionary probably implemented with hashmap, note random output sequence
# size in bytes, Ubuntu Linux 64 bit
numeric_types = {
    # note T capitalized in True
    "boolean": True,                                    # 28
    "int 0": 0,                                         # 24
    "int_max36": 0x7FFFFFFFF,                           # 32
    # explicit line break with \ after operators
    "int 1": \
    1,                                                  # 28
    "int_max32": 0x7FFFFFF,                             # 28
    # 12 bytes hex literal on each line, 36 bytes, 288 bits
    "int_36bytes": ('0x7FFFFFFFFFFFFFFFFFFFFFFF'       # 123
                    'FFFFFFFFFFFFFFFFFFFFFFFF'
                    'FFFFFFFFFFFFFFFFFFFFFFFF'),
    # implied line continuation in parenthesis, brackets, and braces
    "float": 0.0,                                       # 24
    "decimal": decimal.Decimal(0),                      # 104
    "fraction": Fraction(3, 7),                         # 56
    "complex": complex(1, 2.3)                          # 32
}

structures = {
    "dict": dict(),
    "set": set(),
    "str": "a",
    "unicode": u"a",
    "object": object()
}

print("built in types in 64 bit Linux:")
print("numeric types:")

# for k, v in integer_types.items():
for k, v in sorted(numeric_types.items()):
    # use comma to concat strings, int auto convert
    # print("  ", k, ": ", sys.getsizeof(v))
    print('  ', '{:<12}:{:>6}'.format(k, sys.getsizeof(v)))

# Question how to view python source code? e.g. getsizeof() just has return 0

# sys.getsizeof(object[,default]) since 2.6, returns default in case of error
# calls object's __sizeof__ method may add garbage collector overhead
# other modules: numpy.nbyte guppy.hpy pympler.asizeof
# http://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python

print("iterator and sequence types:")

iterator_seqs = {
    "iterator": iter([]),           # 56
    "tuple": tuple(),               # 48
    "list": list(),                 # 64
    "bytearray": bytearray()        # 56
}

for k, v in sorted(iterator_seqs.items()):
    print('  ', '{:<12}:{:>6}'.format(k, sys.getsizeof(v)))
