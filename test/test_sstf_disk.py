from unittest import TestCase

from algorithm.array.sstf_disk import SSTFDisk


class TestSSTFDisk(TestCase):
    def setUp(self):
        self.tbt = SSTFDisk(0)

    def test_next(self):
        self.tbt.add([1, 2, 3])  # queue: [1,2,3], start: 0
        self.assertEqual(self.tbt.next(), 1)  # [2,3], 1
        self.assertEqual(self.tbt.next(), 2)  # [3], 2
        self.tbt.add([1, 2, 3])  # [1,2,3,3]
        self.assertEqual(self.tbt.next(), 2)  # [1,3,3], 2
        self.assertEqual(self.tbt.next(), 1)  # [3,3], 1
        self.assertEqual(self.tbt.next(), 3)  # [3], 3
        self.assertEqual(self.tbt.next(), 3)  # [], 3
        self.assertRaises(RuntimeError, self.tbt.next)
        self.tbt.add([1, 6])  # [1,6], 3
        self.assertEqual(self.tbt.next(), 1)  # [6], 1
