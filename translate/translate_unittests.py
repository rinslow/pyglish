import re

# Asserts
ASSERT_THAT_STAR = "assert that (.+)"
ASSERT_THAT_RAISES = "assert that (.+) raises (.+)"
ASSERT_RAISES = "assert raises (.+):"

# Lists
ASSERT_THAT_IS_ITERABLE = "assert that (.+) is iterable"
ASSERT_THAT_CONTAINS_IN_ORDER = "assert that (.+) contains (.+) in order"


def unittests(code):
    """Translate unit-test piece of codes from pyglish to python.

    Args:
        code (str): pyglish code to translate.

    Returns:
        str. python code.
    """
    # LISTS
    code = re.sub(ASSERT_THAT_CONTAINS_IN_ORDER,
                  r"self.assertTrue(any(\1[i:i+len(\2)]==\2 "
                  r"for i in xrange(len(\1)-len(\2)+1)))",
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

    code = re.sub(ASSERT_THAT_STAR, r"self.assertTrue(\1)", code)

    return code
