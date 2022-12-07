import sys

sys.path.append("../basic-tools")

import unittest

from basic_tools.exceptions import *


class Test_exceptions(unittest.TestCase):
    def test_ClassExistsError_is_Exception(self):
        assert issubclass(
            ClassExistsError, (Exception, BaseException)
        ), f"Is not subclass of BaseException or Exception"

    def test_EmptyDirectoryError_is_Exception(self):
        assert issubclass(
            EmptyDirectoryError, (Exception, BaseException)
        ), f"Is not subclass of BaseException or Exception"
