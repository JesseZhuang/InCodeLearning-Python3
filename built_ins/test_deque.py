'''collections deque, stack, queue'''

from collections import deque
import unittest


class TestDeque(unittest.TestCase):
    '''deque tests'''

    def test_deque_as_stack(self):
        '''use as stack'''
        stack1 = deque()
        for x in [1, 2, 3]:
            stack1.append(x)
        for x in [3, 2, 1]:
            self.assertEqual(x, stack1.pop())

    def test_deque_as_queue(self):
        '''use as stack'''
        queue1 = deque()
        for x in [1, 2, 3]:
            queue1.append(x)
        for x in [1, 2, 3]:
            self.assertEqual(x, queue1.popleft())


if __name__ == '__main__':
    unittest.main()
