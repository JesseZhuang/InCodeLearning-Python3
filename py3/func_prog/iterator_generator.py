"""
https://docs.python.org/3/howto/functional.html?highlight=iterator#generators
Iterator is an object representing a stream of data,
each time returns one element of the data.
It must support  next() or__next__() (special) method,
and raise StopIteration exception when no more element
in the stream.

Generator is a special class of functions simplify the task of writing
iterators. Regular function computes a value and returns it, but generator
returns an iterator that returns a stream of data. It must have yield in
definition block. It can improve program performance by reducing running time
and memory usage.

It is general opinion that generator is always an iterator (not vice versa),
but there is also counterview.
"""


import sys
import time

s = "python"
for w in s:
    print(w)

d = iter(s)
for i in range(len(s)):
    # if range length is longer than len(s),
    # raise StopIteration exception
    print(next(d))     # iterate s
    print((next(iter(s))))    # every time print p, reason?


def even_num(l):
    even_l = []
    for i in l:
        if i % 2 == 0:
            even_l.append(i)
    return even_l
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_num(a))


# generator
def even_num_gen(l):
    for i in l:
        if i % 2 == 0:
            yield i
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = even_num_gen(b)
print(even_num_gen(b))  # yield even number
print(next(c))  # 2
print(next(c))  # 4
print(next(c))  # 6
print(next(c))  # 8
# print(next(c))  raise StopIteration exception

e = [x for x in range(1000000)]
b_time_list = time.clock()
e_list = even_num(e)
e_time_list = time.clock()
print(sys.getsizeof(e_list))
print('Time costs {} seconds.'.format(e_time_list - b_time_list))

b_time_gen = time.clock()
e_gen = even_num_gen(e)
e_time_gen = time.clock()
print(sys.getsizeof(e_gen))
print('Time costs {} seconds.'.format(e_time_gen - b_time_gen))

# sys.getsizeof() return the size of an object in bytes.
