# tuple is immutable list
a_tuple = ("a", "b", "mpilgrim", "z", "example")
print(a_tuple[0])
print(a_tuple[-1])
print(a_tuple[1:3])

# immutable
try:
    a_tuple.append('new')
except AttributeError:
    print("no append method defined for tuples")

# benefits: faster, safer, as dict keys
print("======conversion tuple list======")
a_list = list(a_tuple)   # list() thaws a tuple
print(a_list)
print(tuple(a_list))     # tuple() freezes a list

print("======assigning multiple values======")
three_values = ('a', 2, True)
x, y, z = three_values
print(x, y, z)
(x, y, z) = three_values
print(x, y, z)

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(MONDAY)
