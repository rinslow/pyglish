import re

# Asserts
ASSERT_THAT_STAR = "assert that (.+)"
ASSERT_THAT_IS = "assert that (.+) is (.+)"
ASSERT_THAT_RAISES = "assert that (.+) raises (.+)"
ASSERT_RAISES = "assert raises (.+):"

# Comparisons
ASSERT_THAT_EQUAL_TO = "assert that (.+) is equal to (.+)"
ASSERT_THAT_NOT_EQUAL_TO = "assert that (.+) is not equal to (.+)"
ASSERT_THAT_GREATER_THAN = "assert that (.+) is greater than (.+)"
ASSERT_THAT_GREATER_EQUALS = "assert that (.+) is greater than or equal to (.+)"
ASSERT_THAT_LESS_THAN = "assert that (.+) is less than (.+)"
ASSERT_THAT_LESS_EQUALS = "assert that (.+) is less than or equal to (.+)"
ASSERT_THAT_BETWEEN = "assert that (.+) is between (.+) and (.+)"

# Lists
ASSERT_THAT_IN = "assert that (.+) is in (.+)"
ASSERT_THAT_CONTAINS = "assert that (.+) contains (.+)"
ASSERT_THAT_IS_ITERABLE = "assert that (.+) is iterable"
ASSERT_THAT_CONTAINS_IN_ORDER = "assert that (.+) contains (.+) in order"


def unittests(code):
    """Translate unit-test piece of codes from pyglish to python.

    Args:
        code (str): pyglish code to translate.

    Returns:
        str. python code.
    """
    # COMPARISONS
    code = re.sub(ASSERT_THAT_EQUAL_TO,
                  r"self.assertEqual(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_NOT_EQUAL_TO,
                  r"self.assertNotEqual(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_GREATER_EQUALS,
                  r"self.assertGreaterEqual(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_GREATER_THAN,
                  r"self.assertGreater(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_LESS_EQUALS,
                  r"self.assertLessEqual(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_LESS_THAN,
                  r"self.assertLess(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_BETWEEN,
                  r"self.assertTrue(\2 <= \1 <= \3)",
                  code)

    # LISTS
    code = re.sub(ASSERT_THAT_CONTAINS_IN_ORDER,
                  r"self.assertTrue(any(\1[i:i+len(\2)]==\2 "
                  r"for i in xrange(len(\1)-len(\2)+1)))",
                  code)

    code = re.sub(ASSERT_THAT_CONTAINS,
                  r"self.assertIn(\2, \1)",
                  code)

    code = re.sub(ASSERT_THAT_IN,
                  r"self.assertIn(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_IS_ITERABLE,
                  r"import collections; self.assertTrue(isinstance(\1, "
                  r"collections.Iterable))",
                  code)
    # GENERAL
    code = re.sub(ASSERT_THAT_RAISES,
                  r"self.assertRaises(\1, \2)",
                  code)

    code = re.sub(ASSERT_RAISES,
                  r"with self.assertRaises(\1):",
                  code)

    code = re.sub(ASSERT_THAT_IS,
                  r"self.assertIs(\1, \2)",
                  code)

    code = re.sub(ASSERT_THAT_STAR, r"self.assertTrue(\1)", code)

    return code
