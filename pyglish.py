"""English readable python language."""
import os
import sys

from errors import FileDoesNotEndWithPYG

from translate.translate_unittests import unittests
from translate.translate_loops import loops
from translate.translate_comparisons import comparisons


TRANSLATORS = [unittests, loops, comparisons]


def translate(code):
    """Translate a piece of pyglish code into python code.

    Args:
        code (str): original pyglish code.

    Returns:
        str. output python code.
    """
    for translator in TRANSLATORS:
        code = translator(code)

    return code


def run(pyg_path, should_execute=True):
    """Create and run a .py file from a .pyg file.

    Args:
        pyg_path (str): path to a .pyg file.
        should_execute (bool): whether to execute new .pyg file or not.
    """
    py_path = pyg_path[:-1]

    if not pyg_path.endswith(".pyg"):
        raise FileDoesNotEndWithPYG(pyg_path)

    with open(py_path, "w") as py_file, open(pyg_path, "r") as pyg_file:
        pyg_code = pyg_file.read()
        py_code = translate(pyg_code)
        py_file.write(py_code)

    if should_execute:
        os.system("python %s" % py_path)

if __name__ == '__main__':
    run(sys.argv[1])  # TODO: Make it possible to translate a project.
