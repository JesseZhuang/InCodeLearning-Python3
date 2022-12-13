# C source https://github.com/python/cpython/blob/master/Include/listobject.h
# dynamic array, not linked list
# Array can only contain same type items,
# list is mutable
# using list as a queue, not efficient
queue = [0, 1, 2, 3, 4]
queue.append(5)
queue.append(6)
print(queue)
queue.pop(0)
print(queue)  # elements 1-6 shifted left by one O(n) time

l = [True, 2, 3.5, 5 - 8j, [9, 7, 5], 'python', ('a', 2)]

print(hex(id(l)))  # 0x2564cb0  memory address (32 bit?), machine dependent.
print(len(l))  # 7

# slicing, not including the second slice index
print(l[:5])  # [True, 2, 3.5, 5-8j, [9, 7, 5]],

# list index
print(l[0])  # True
print(l[-7])  # True    list[-n] == list[len(list) - n]
# print(l[-8]) Error, index out of range, not intuitive

print(l[4:-1])  # [[9, 7, 5], 'python'], combination of pos & neg index
print(l[4:-6])  # [], if 2nd slice index on the left of 1st one
print("4:-8", l[4:-8])  # not intuitive, no error
print(l[6:3])  # [], same reason as above one

print("======adding items to a list======")
print(l + ['concat', 'at', 'end'])    # list concat, create a new list
l.append([1, 2, 3])  # add a sublist
print(l)
# [True, 2, 3.5, (5-8j), [9, 7, 5], 'python', ('a', 2), [1, 2, 3]]

l.extend([4, 5, 'a'])  # add three numbers
print(l)
# [True, 2, 3.5, (5-8j), [9, 7, 5], 'python', ('a', 2), [1, 2, 3], 4, 5, 'a']

l.insert(0, 'a')  # assign item to specific position
print(l)

print("======searching for values in a list======")
print(l.count('a'))  # 2, return # how many items that item shows in the list
print(l.count(2))  # 1, item in the sublist is not counted

print(l.index('a'))  # return to the first match item

# -1 is valid index for list, raise exception is better than return -1
try:
    print('a is in l', l.index('a'))
    print(l.index('not in l'))
except ValueError:
    print('"not in l" is not in l')

print("======removing list items======")
l.remove('a')  # delete the first match item
print(l)
# [True, 2, 3.5, (5-8j), [9, 7, 5], 'python', ('a', 2), [1, 2, 3], 4, 5, 'a']

del l[1]

l.pop()  # remove the last item
print(l)
# [True, 2, 3.5, (5-8j), [9, 7, 5], 'python', ('a', 2), [1, 2, 3], 4, 5]

# print(l.sort()) exception, TypeError: unorderable types: complex() < float()
l.remove(l[3])  # remove assigned index item
print(l)  # [True, 2, 3.5, [9, 7, 5], 'python', ('a', 2), [1, 2, 3], 4, 5]

# print(l.sort())  TypeError: unorderable types: list() < float(),
# l.sort() should be used in homogeneous type list
l.pop(3)  # remove the assigned index item, l.pop(1) or l.pop([1])
l.pop(-3)
l.pop(-3)
print(l)  # [True, 2, 3.5, 'python', 4, 5]

print(hex(id(l)))  # 0x2584cb0, same as previous.

ls = [i for i in range(5)]
print(ls)  # [0, 1, 2, 3, 4]
print(hex(id(ls)))  # 0x764cd8
ls.sort(reverse=True)
print(ls)  # [ 4, 3, 2, 1, 0]

l_string = ['a', 'p', 'Python', 'C', 'c#', 'c++']
l_string.sort()
print(l_string)  # ['C', 'Python', 'a', 'c#', 'c++', 'p']
l_str = [i.lower() for i in l_string]
print(l_str)  # ['c', 'python', 'a', 'c#', 'c++', 'p']
l_str.sort()
print(l_str)  # ['a', 'c', 'c#', 'c++', 'p', 'python']

l2 = [4, 3, 2, 1, 0]
print(hex(id(l2)))  # 0x554d50
print(ls == l2)  # True, the comparison is not address, but content

l.reverse()
print(l)  # [5, 4, 'python', 3.5, 2, True]

# Todo compare shallow deepcopy
l_new = l.copy()
l_new2 = l[:]
print(l_new, l_new2)
# [5, 4, 'python', 3.5, 2, True] [5, 4, 'python', 3.5, 2, True]
print(hex(id(l)), hex(id(l_new)), hex(id(l_new2)))
# memory addresses are different.


# A tuple is an immutable list. Once it is created, it can not be changed.
# Except the method, which will change the content of the List,
# such as insert(), extend(), remove()etc, Tuple can use the methods of List.
