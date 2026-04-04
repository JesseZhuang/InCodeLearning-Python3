import unittest

from algorithm.ood.excel_sum_formula import Excel, Excel2


class TestExcelSumFormula(unittest.TestCase):
    def setUp(self):
        self.implementations = [Excel, Excel2]

    def verify(self, commands, arguments, expected):
        for excel_cls in self.implementations:
            with self.subTest(excel=excel_cls.__name__):
                result = []
                sheet = None
                for command, args in zip(commands, arguments):
                    if command == "Excel":
                        sheet = excel_cls(*args)
                        result.append(None)
                    else:
                        result.append(getattr(sheet, command)(*args))
                self.assertEqual(expected, result)

    def test_example(self):
        self.verify(
            ["Excel", "set", "sum", "set", "get"],
            [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]],
            [None, None, 4, None, 6],
        )

    def test_overwrite_formula_with_raw_value(self):
        self.verify(
            ["Excel", "set", "set", "sum", "get", "set", "set", "get"],
            [[2, "C"], [1, "A", 5], [1, "B", 3], [2, "C", ["A1:B1"]], [2, "C"],
             [2, "C", 100], [1, "A", 20], [2, "C"]],
            [None, None, None, 8, 8, None, None, 100],
        )

    def test_replace_formula_and_update_chain(self):
        self.verify(
            ["Excel", "set", "set", "sum", "sum", "get", "sum", "get", "set", "get",
             "get", "set", "get", "get"],
            [[2, "D"], [1, "A", 2], [1, "B", 3], [1, "C", ["A1", "A1:B1"]],
             [2, "A", ["C1", "B1"]], [2, "A"], [1, "C", ["B1"]], [2, "A"],
             [1, "A", 10], [1, "C"], [2, "A"], [1, "B", 5], [1, "C"], [2, "A"]],
            [None, None, None, 7, 10, 10, 3, 6, None, 3, 6, None, 5, 10],
        )

    def test_overlapping_ranges_count_multiple_times(self):
        self.verify(
            ["Excel", "set", "set", "set", "set", "sum", "set", "get"],
            [[3, "D"], [1, "A", 1], [1, "B", 2], [2, "A", 3], [2, "B", 4],
             [3, "D", ["A1:B2", "B1:B2"]], [2, "B", 5], [3, "D"]],
            [None, None, None, None, None, 16, None, 18],
        )
