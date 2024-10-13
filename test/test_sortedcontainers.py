import unittest

from sortedcontainers import SortedList


class TestSortedContainers(unittest.TestCase):

    def test_sortedlist_key(self):
        class Foo:
            def __init__(self, id: int, name: str):
                self.id = id
                self.name = name

            def __repr__(self):
                return f"Foo({self.id}, {self.name})"

        foo1, foo2 = Foo(1, 'foo'), Foo(2, 'bar')
        s1 = SortedList([foo1, foo2], key=lambda x: x.id)
        # sort by id
        self.assertIs(s1[0], foo1)
        self.assertIs(s1[1], foo2)
        s2 = SortedList([foo1, foo2], key=lambda x: x.name)
        self.assertIs(s2[1], foo1)
        self.assertIs(s2[0], foo2)
