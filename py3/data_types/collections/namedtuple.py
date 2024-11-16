"""
https://docs.python.org/3.5/library/collections.html?highlight=collections

8.3.5. namedtuple() Factory Function for Tuples with Named Fields
"""

from collections import namedtuple


##############################################################################
# purpose:
# - assign meaning to each position in a tuple
#   - can be used as a tuple
#   - can be accessed by field names

##############################################################################
#  creation
# creates a tuple subclass

Animal = namedtuple(
    typename='Animal',
    field_names='type shape',
    verbose=False,
    rename=False
)

##########
# typename: valid identifiers:
#
#   CONTAINS:
#       - letters, digits, underscores
#   DOES NOT START WITH:
#       - digits
#   CANNOT BE:
#       - a keyword
#           - class, for, return, global, pass, raise

for bad_typename in (
    'Animal!',
    '0Animal',
    # keywords: there are 33 of them, in `keyword.kwlist`
    'class',
    'for',
    'return',
    'global',
    'pass',
    'raise'
):
    try:
        BadTypename = namedtuple(bad_typename, 'type shape')
    except ValueError as error:
        message = 'Got error for bad_typename={}: {}'.format(bad_typename,
                                                             str(error))
        print(message)

# starting with underscore is fine
UnderscoreAnimal = namedtuple('_Animal', 'type shape')


##########
# fieldnames:

###
# equivalent formats

Animal_0 = namedtuple('Animal', 'type shape')
Animal_1 = namedtuple('Animal', 'type, shape')
Animal_2 = namedtuple('Animal', ['type', 'shape'])

###
# field_names: valid identifiers + must not start with underscores

for bad_fieldname in (
    'type!',
    '0type',
    '_type',
    'class'
):
    try:
        BadFieldNameAnimal = namedtuple('Animal', bad_fieldname)
    except ValueError as error:
        message = 'Got error for bad_fieldname={}: {}'.format(bad_fieldname,
                                                              str(error))
        print(message)


cat = Animal(type='Cat', shape='Fat')
dog = Animal(type='Dog', shape='Slim')
print(cat)
print(dog)


# namedtuple as a better way to return multiple outputs

# use traditional tuples
def x():
    return 'cat', 'fat'


result = x()
print(result[0])
print(result[1])

# can also take advantage of unpacking
animal_type, animal_shape = x()


# return a namedtuple to make return value more explicit
def readable_x():
    return Animal(type='cat', shape='fat')


result = readable_x()
print(result.type)
print(result[0])
