import unittest


# command line interface usage
# python -m unittest test_module1 test_module2
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method
# python -m unittest [discover] [-v|-s|-p|-t], finds all tests named test*.py


class FooTestSetupTearDown(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    # http://www.drdobbs.com/testing/unit-testing-with-python/240165163?pgno=2
    # Learning point 1: setUp and tearDown are TestCase methods
    # Learning point 2: setUp and tearDown sequence for each TC
    # Learning point 3: self.shortDescription() for TC-Setup communication
    # Learning point 4: each TC must have a Test Route (assert)
    # Learning point 5: test suite is a collection of test cases
    # Learning point 6: ignore TC, failed TC

    def setUp(self):
        """ Setting up for the test """
        print("FooTest:setUp_:begin")
        # do something begin ...
        testname = self.shortDescription()  # takes docstring from testcase
        if testname == "Test routine A":
            print("setting up for test A")
        elif testname == "Test routine B":
            print("setting up for test B")
        else:
            print("Unknown Test Routine")
        # do something end ...
        print("FooTest:setUp_:end")

    def tearDown(self):
        """Cleaning up after the test"""
        print("FooTest:tearDown_:begin")

        # do sth begin ...
        testname = self.shortDescription()

        if testname == "Test routine A":
            print("teardown for test A")
        elif testname == "Test routine B":
            print("teardown for test B")
        else:
            print("Unknown Test Routine")
        print("FooTest:tearDown_:end")

    def testLogic(self):
        """Test routine A"""

        print("FooTest:testA")
        # todo: Logic Assertion: assertTrue, assertEqual,
        #        assertIs, assertIsNone, assertIsInstance
        self.assertTrue(True)
        self.assertEqual("narf", "narf", "They are the same")
        self.assertNotEqual(123, "123")

        # todo: Sample of assertGreater, assertAlmostEqual,
        self.assertGreater(456, 123, "456 is greater than 123")

    def testCollections(self):
        """Test routine B"""

        # todo: dict, lists, sets, and tuples Assertions
        # assertIn, assertDictEqual, assertListEqual, assertSetEqual,
        # assertSquenceEqual, assertTupleEqual, assertMultiplelineEqual

        argFoo = {'narf': 456, 'poink': 789}
        argBar = {'narf': 456, 'poink': 789}
        # Todo: assertDictContainsSubset deprecated, find replacement
        # self.assertDictContainsSubset(argFoo, argBar)
        print("FooTest:testB")


@unittest.skip("Skip ove the entire FooTest routine")
class FooTest(unittest.TestCase):
    def tc1(self):
        """FooTest:test1"""
        self.assertTrue(True)
        print("Running FooTest:test1")


@unittest.skip("Skip ove the entire BarTest routine")
class BarTest(unittest.TestCase):
    def tc1(self):
        """Test BarTest tc1"""
        self.skipTest("Skip over the rst of the test")
        # use fail when you know the feature is not ready to be tested yet
        self.fail("Force this routine to fail")
        self.assertFalse(False)
        print("Running BarTest")


# create/add/execute a test suite (todo report a testsuite )
newSuite = unittest.TestSuite()
newSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(FooTest))
newSuite.addTest(FooTest("tc1"))
newSuite.addTest(BarTest("tc1"))

fooRunner = unittest.TextTestRunner(descriptions=True)
fooRunner.run(newSuite)

# ss in output signals the two skipped tests
# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
# if import this module, all the print statements will not show

if __name__ == '__main__':
    unittest.main()
    # Todo: with line below did not see run 2 tests twice
    fooSuite = unittest.TestLoader().loadTestsFromTestCase(FooTest)
