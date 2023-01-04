'''old mission OA'''

# pylint: disable-all

import math
import math  # safe to re-import, use cache
import subprocess

d = {None: None, None: None}
print(d)


def method1(d, k, v):
    if isinstance(d, dict):
        d[k] = v


def method2(d, k, v):
    try:
        d[k] = v
    except TypeError:
        pass


x = [1, 2, 3]

print("reverse1", x.copy().reverse())  # reverse in place
print(x.copy()[::-1])
print(sorted(x.copy(), reverse=True))


d = {'a': 'a1'}

t = dict()
t.update(d)

t['secret'] = 'a1b2'
print(t)
print(d)

t = d
t['secret'] = 'a1b2'
print(t)
print(d)

print('Hello, World!'[-9::3])


class Parent(object):
    def __fun(self):
        print('fun')


class Child(Parent):
    pass


c = Child()
# c.__fun

p = Parent()
# p.__fun


# out = 'out.log'
# subprocess.call(['touch', out])
# with open(out, 'a') as fd:
#     fd.write('Hello')

if __name__ == '__main__':
    import math
    print(max(1, 2))
    pass


class Foo(object):
    def __init__(self) -> None:
        self._bar = 1

    @property
    def bar(self):
        # location 1
        return self._bar

    def bar1(self, a):
        print('bar1', a)

    def bar1(self, a, b):
        print('bar12', a, b)

# pyc benefit


FOO = 'foo56'

print(f'{FOO:>5.6}')

# python 2 3 devision, prefer floor division?


f = Foo()
# f.bar1('mm', 'mmm')
# f.bar1('mm')


def solution(str1):
    '''calculate fee for phone calls'''
    lines = str1.splitlines()
    calls = dict()
    max_seconds = 0
    free_phone = ''
    for line in lines:
        phone = line[9:]
        seconds = convert_time(line[:8])
        if seconds >= max_seconds:
            free_phone = phone
            max_seconds = seconds
        if phone in calls:
            calls[line[9:]] += seconds
        else:
            calls[line[9:]] = seconds
    print(calls)
    print(free_phone)
    fee = 0
    for (k, v) in calls.items():
        if k != free_phone:
            fee += calculate(v)
    print(fee)
    return fee


def convert_time(time_s):
    '''convert string to seconds'''
    seconds = 0
    seconds += int(time_s[:2]) * 3600
    seconds += int(time_s[3:5]) * 60
    seconds += int(time_s[6:])
    return seconds


def calculate(seconds):
    '''calcualte fee'''
    if seconds >= 300:
        return seconds // 60 * 150
    return seconds * 3


solution('''00:01:07,400-234-090
00:05:01,701-080-080
00:05:00,400-234-090''')  # 900, 701-080-080 free
# 3 cents/second if < 5min, 150 cents if > 5min, each call (maybe each numnber) calculates seprately
# one free call with most time, if same time, the smaller number is free

# pyc files
