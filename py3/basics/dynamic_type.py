import sys
# From Book Learning Python by Mark Lutz
# 1.variable VS object
a = 3        # Assign a name to an object

# variables and objects are stored in different parts of memory
# Variables always link to objects and never to other variables
# larger objects may link to other objects
# Variables are entries in a system table, with spaces for links to objects.
# Objects are pieces of allocated memory, with enough space for values
# References are automatically followed pointers from variables to objects.

# 2.Types Live with Objects, Not Variables

x = 42
x = 'shrubbery'
# Reclaim 42 now (unless referenced elsewhere)
x = 3.1415      # Reclaim 'shrubbery' now
x = [1, 2, 3]   # Reclaim 3.1415 now

# object is garbage collected like java when no reference found.
# Python accomplishes this feature by keeping a counter in every object

# 3. Shared references

L1 = [2, 3, 4]  # A mutable object
L2 = L1  # Make a reference to the same object
L1[0] = 24  # An in-place change

print(L1)  # [24, 3, 4]  # L1 is different
print(L2)  # [24, 3, 4]  # But so is L2!

L1 = [2, 3, 4]
L2 = L1[:]   # Make a copy of L1 (or list(L1), copy.copy(L1), etc.)
L1[0] = 24

print(L1)     # [24, 3, 4]
print(L2)     # L2 is not changed [2, 3, 4]

L = [1, 2, 3]
M = [1, 2, 3]
print(L == M)
print(L is M)      # Different objects

X = 42
Y = 42
print(X == Y)
print(X is Y)      # Same object anyhow: caching at work!


# Python caches and reuses small integers and small strings
# http://stackoverflow.com/questions/306313/
# is-operator-behaves-unexpectedly-with-integers
# and stackoverflow questions 15171695, 21091568
# you can always ask Python how many references there are to an object:
print(sys.getrefcount(1))
# get different numbers on different systems
