import unittest

from algorithm.ood.codesignal_demo import solution


class TestCodeSignalDemo(unittest.TestCase):

    def test_solution_level1(self):
        cases = [["ADD", "10"],
                 ["ADD", "100"]]
        exp = ["1", "2"]
        self.assertEqual(solution(cases), exp)

    def test_solution_level2(self):
        cases = [
            [["ADD", "5"],
             ["ADD", "3"],
             ["ADD", "5"],
             ["ADD", "5"],
             ["ADD", "10"],
             ["ADD", "3"],
             ["GET_MEDIAN"],
             ["ADD", "3"],
             ["ADD", "3"],
             ["ADD", "3"],
             ["GET_MEDIAN"]],

            [["ADD", "10"],
             ["ADD", "20"],
             ["GET_MEDIAN"],
             ["ADD", "30"],
             ["ADD", "40"],
             ["GET_MEDIAN"],
             ["GET_MEDIAN"],
             ["ADD", "50"],
             ["ADD", "60"],
             ["ADD", "70"],
             ["ADD", "80"],
             ["GET_MEDIAN"]]
        ]
        exps = [
            ["1",
             "2",
             "3",
             "4",
             "5",
             "6",
             "5",
             "7",
             "8",
             "9",
             "3"],

            ["1",
             "2",
             "10",
             "3",
             "4",
             "20",
             "20",
             "5",
             "6",
             "7",
             "8",
             "40"]
        ]
        for c, exp in zip(cases, exps):
            with self.subTest(c):
                self.assertEqual(solution(c), exp)
