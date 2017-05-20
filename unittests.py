from unittest import TestCase
from translate.translate_unittests import unittests as ut


class UnittestCase(TestCase):
    def test_assertThat(self):
        code = "assert that x == y"
        expected = "self.assertTrue(x == y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsEqualTo(self):
        code = "assert that x is equal to y"
        expected = "self.assertEqual(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsNotEqualTo(self):
        code = "assert that x is not equal to y"
        expected = "self.assertNotEqual(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsGreaterThan(self):
        code = "assert that x is greater than y"
        expected = "self.assertGreater(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsGreaterThanOrEqualTo(self):
        code = "assert that x is greater than or equal to y"
        expected = "self.assertGreaterEqual(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsLessThan(self):
        code = "assert that x is less than y"
        expected = "self.assertLess(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsLessThanOrEqualTo(self):
        code = "assert that x is less than or equal to y"
        expected = "self.assertLessEqual(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatIsBetween(self):
        code = "assert that x is between 0 and 9"
        expected = "self.assertTrue(0 <= x <= 9)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertIs(self):
        code = "assert that x is y"
        expected = "self.assertIs(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertIn(self):
        code = "assert that x is in y"
        expected = "self.assertIn(x, y)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertContains(self):
        code = "assert that x contains y"
        expected = "self.assertIn(y, x)"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertIsIterable(self):
        code = "assert that x is iterable"
        expected = "import collections; " \
                   "self.assertTrue(isinstance(x, collections.Iterable))"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertContainsInOrder(self):
        code = "assert that [1, 2, 3] contains [2, 3] in order"
        eval(ut(code))
        with self.assertRaises(AssertionError):
            code = "assert that [1, 2, 3] contains [1, 3] in order"
            eval(ut(code))

    def test_assertRaises(self):
        code = "assert raises MeowException:"
        expected = "with self.assertRaises(MeowException):"
        actual = ut(code)
        self.assertEquals(expected, actual)

    def test_assertThatRaises(self):
        code = "assert that foo raises MeowException"
        expected = "self.assertRaises(foo, MeowException)"
        actual = ut(code)
        self.assertEquals(expected, actual)