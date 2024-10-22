import unittest

from sortedcontainers import SortedList


class Foo:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Foo({self.id}, {self.name})"


class TestSortedContainers(unittest.TestCase):

    def test_sortedlist_key(self):
        foo1, foo2 = Foo(1, 'foo'), Foo(2, 'bar')
        s1 = SortedList([foo1, foo2], key=lambda x: x.id)
        # sort by id
        self.assertIs(s1[0], foo1)
        self.assertIs(s1[1], foo2)
        s2 = SortedList([foo1, foo2], key=lambda x: x.name)
        self.assertIs(s2[1], foo1)
        self.assertIs(s2[0], foo2)

    def test_sortedlist_bisect(self):
        foo1, foo2 = Foo(1, 'foo'), Foo(2, 'bar')
        s1 = SortedList(key=lambda x: (x.id, x.name))
        s1.add(foo1)
        s1.add(foo2)
        dummy1, dummy2 = Foo(1, 'dummy'), Foo(2, 'dummy')
        self.assertEqual(1, s1.bisect_right(foo1))
        self.assertEqual(2, s1.bisect_right(foo2))
        self.assertEqual(0, s1.bisect_right(dummy1))
        self.assertEqual(2, s1.bisect_right(dummy2))
        s1.add(dummy1)
        self.assertIs(dummy1, s1[0])
        self.assertEqual(1, s1.bisect_right(dummy1))
