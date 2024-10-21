from unittest import TestCase

from algorithm.ood.in_memory_db import solution


class TestInMemoryDB(TestCase):
    def test_level1(self):
        queries = [
            ["SET", 0, "A", "B", 4],
            ["SET", 1, "A", "C", 6],
            ["COMPARE_AND_SET", 2, "A", "B", 4, 9],
            ["COMPARE_AND_SET", 3, "A", "C", 4, 9],
            ["COMPARE_AND_DELETE", 4, "A", "C", 6],
            ["GET", 5, "A", "C"],
            ["GET", 6, "A", "B"],
        ]
        expected = [
            None,
            None,
            True,  # A.B 4->9
            False,  # A.C 4!=6
            True,  # deleted A.C:6
            None,  # deleted
            9,
        ]
        self.assertEqual(expected, solution(queries))
        queries = [
            ["SET", 160000000, "a", "a", 1],
            ["SET", 160000001, "a", "A", 2],
            ["GET", 160000002, "a", "a"],
            ["COMPARE_AND_DELETE", 160000003, "a", "a", 0],
            ["GET", 160000004, "a", "a"],
            ["COMPARE_AND_DELETE", 160000005, "a", "a", 1],
            ["GET", 160000006, "a", "a"],
            ["GET", 160000007, "a", "A"],
            ["COMPARE_AND_DELETE", 160000008, "a", "A", 2],
            ["SET", 160000009, "a", "A", 7],
            ["SET", 160000010, "a", "A", 9],
            ["GET", 160000011, "a", "a"],
            ["GET", 160000012, "a", "A"]
        ]
        expected = [
            None,
            None,
            1,  # a.a 1
            False,  # a.a != 0
            1,
            True,  # deleted a.a:1
            None,  # a.a deleted
            2,
            True,  # deleted a.A:2
            None,
            None,
            None,  # a.a deleted
            9
        ]
        self.assertEqual(expected, solution(queries))

    def test_level3(self):
        queries = [
            ["SET", 1, "A", "B", 4],
            ["SET_WITH_TTL", 2, "X", "Y", 5, 15],
            ["SET_WITH_TTL", 4, "A", "D", 3, 6],
            ["COMPARE_AND_SET_WITH_TTL", 6, "A", "D", 3, 5, 10],
            ["GET", 7, "A", "D"],
            ["SCAN", 15, "A"],
            ["SCAN", 17, "A"]
        ]
        expected = [
            None,
            None,
            None,
            True,  # A.D:3->5 ttl:6+10
            5,
            ["B(4)", "D(5)"],
            ["B(4)"],  # D(5) expires on 16
        ]
        self.assertEqual(expected, solution(queries))

    def test_level4(self):
        queries = [
            ["SET_AT_WITH_TTL", "A", "B", 1, 1, 10],
            ["BACKUP", 3],
            ["SET_AT", "A", "D", 2, 4],
            ["BACKUP", 5],  # A.B(1) remaining ttl 6
            ["DELETE_AT", "A", "B", 8],
            ["BACKUP", 9],
            ["RESTORE", 10, 7],
            ["BACKUP", 11],
            ["SCAN_AT", "A", 15],
            ["SCAN_AT", "A", 16]
        ]
        expected = [
            None,
            1,  # backup one record A.B(1)
            None,
            1,  # backup one record A.B(1) A.D(2)
            True,
            1,  # backup one record A.D(2)
            None,
            1,  # backup one record A.B(1) A.D(2)
            ["B(1)", "D(2)"],
            ["D(2)"],  # A.B(1) expires on 16
        ]
        self.assertEqual(expected, solution(queries))
