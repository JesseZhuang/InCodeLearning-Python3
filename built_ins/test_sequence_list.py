'''
python list
C source https://github.com/python/cpython/blob/master/Include/listobject.h
dynamic array, not linked list
array can only contain same type items, list is mutable
'''


import unittest


l = [True, 2, 3.5, 5 - 8j, [9, 7, 5], 'python', ('a', 2)]

# 0x2564cb0  memory address (32 bit?), machine dependent. 0x7ff661c16dc0 on 64 bit
print(hex(id(l)))

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


def reverse_list_inplace(a_list: list) -> list:
    '''reverse a list in place'''
    a_list.reverse()
    return a_list


class TestSequenceList(unittest.TestCase):
    '''python built-in list'''

    def test_copy_list(self):
        '''copy list'''
        list1 = list(range(10))
        list2 = list1.copy()
        self.assertEqual(list1, list2)
        self.assertNotEqual(id(list1), id(list2))
        list3 = list1[:]
        self.assertEqual(list1, list3)
        self.assertNotEqual(id(list1), id(list3))

    def test_use_as_queue(self):
        '''use list as queue'''
        queue = [0, 1, 2, 3, 4]
        queue.append(5)  # ok, amortized constant time
        queue.append(6)
        self.assertEqual(7, len(queue))
        queue.pop(0)  # elements 1-6 shifted left by one O(n) time
        self.assertEqual(6, len(queue))

    def test_using_range(self):
        '''natural number list'''
        self.assertEqual([2, 3, 4], list(range(2, 5)))

    def test_create_list_filled(self):
        '''create a list filled with same value'''
        self.assertEqual([1, 1, 1, 1, 1], [1] * 5)

    def test_reverse_list_inplace(self):
        '''passed in list is reversed'''
        list1 = [1, 2, 3]
        self.assertEqual([3, 2, 1], reverse_list_inplace(list1))
        self.assertEqual([3, 2, 1], list1)

    def test_reversed(self):
        '''reversed() get a reversed iterator on the orignal copy'''
        list1 = [1, 2, 3]
        reversed_list1 = reversed(list1)
        self.assertEqual('list_reverseiterator', type(reversed_list1).__name__)
        list1[-1] = 4
        self.assertEqual(4, next(reversed_list1))
        self.assertEqual(2, next(reversed_list1))

        list2 = list(reversed_list1)
        self.assertEqual([1], list2)

        list3 = list(reversed(list1))
        self.assertEqual([4, 2, 1], list3)


if __name__ == '__main__':
    unittest.main()
