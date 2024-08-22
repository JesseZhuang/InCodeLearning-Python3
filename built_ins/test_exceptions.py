"""test exceptions"""

import unittest


class TestException(unittest.TestCase):
    """test exception related"""

    def test_re_throw_exception(self):
        def raise_exc():
            raise Exception("something happened")

        def re_throw_same():
            try:
                raise_exc()
            except Exception as e:
                print("exception caught:", e)
                raise  # re-throw same exception

        self.assertRaises(Exception, re_throw_same)


if __name__ == '__main__':
    unittest.main()
