import unittest
# to use both python test.py and python -m unittest
try:
    from . import everything_object
# above works when running python -m unittest from repo base directory
# or python -m basics.test_everything_object
except ImportError:
    import everything_object
# running python test_everyting_object.py in basics dir
# for more see stackoverflow 16981921/relative-imports-in-python-3


class TestEverythingObject(unittest.TestCase):
    """
    Testing everything_object.py first class everything in python.
    """

    @classmethod
    def setUpClass(cls):
        cls.list1 = [1, 2, 3]

    def setUp(self):
        self.fun_object = everything_object.i_am_an_object

    def test_setup(self):
        self.__class__.list1.pop()
        print('modified class variable in setup', self.__class__.list1)

    def test_setup2(self):
        self.__class__.list1.pop()
        print('modified class variable in setup2', self.__class__.list1)

    def test_assign_to_var(self):
        self.assertEqual(self.fun_object, everything_object.i_am_an_object,
                         'function not equal to assigned variable')
        self.assertEqual(self.fun_object(1), 1, 'function should return'
                         'argument directly')

    def test_higher_order(self):
        self.assertEqual(everything_object.cubic(everything_object.square,
                         2), 8, "cubic of 2 should be 8")

    def test_higher_oder_sort(self):
        zepp = [('Guitar', 'Jimmy'), ('Vocals', 'Robert'), ('Bass',
                'John Paul'), ('Drums', 'John')]
        self.assertEqual(sorted(zepp, key=everything_object.second_element),
                         [('Guitar', 'Jimmy'), ('Drums', 'John'), ('Bass',
                          'John Paul'), ('Vocals', 'Robert')],
                         "should sort with second tuple element as key")

    def tearDown(self):
        self.fun_object = None


# every module is an object having an attribute __name__
print(everything_object.__name__)  # everything_object or basics.everything_object
print(__name__)  # __main__ or basics.test_everything_object

# necessary when running python basics/test_everything_object.py
if __name__ == '__main__':
    unittest.main()
