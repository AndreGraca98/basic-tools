import sys

sys.path.append("../basic-tools")

import unittest

from basic_tools.assertions import *


class Test_assert_xor(unittest.TestCase):
    def test_assert_xor_val_none(self):
        a = 1
        b = None
        assert_xor(a, b)

    def test_assert_xor_val_val(self):
        with self.assertRaises(ValueError):
            a = 1
            b = 1
            assert_xor(a, b)

    def test_assert_xor_none_none(self):
        with self.assertRaises(ValueError):
            a = None
            b = None
            assert_xor(a, b)


class Test_assert_range(unittest.TestCase):
    def test_assert_range_in_range(self):
        value = 2
        m = 1
        M = 3
        assert_range(
            value=value,
            m=m,
            M=M,
        )

    def test_assert_range_outside_min(self):
        with self.assertRaises(ValueError):
            value = 0.5
            m = 1
            M = 3
            assert_range(
                value=value,
                m=m,
                M=M,
            )

    def test_assert_range_outside_max(self):
        with self.assertRaises(ValueError):
            value = 3.5
            m = 1
            M = 3
            assert_range(
                value=value,
                m=m,
                M=M,
            )


class Test_assert_types(unittest.TestCase):
    def test_assert_types_correct_type(self):
        value = 2
        assert_types(value, int)

    def test_assert_types_no_types(self):
        with self.assertRaises(ValueError):
            value = 2
            assert_types(value=value)

    def test_assert_types_wrong_types(self):
        with self.assertRaises(TypeError):
            value = 2
            assert_types(value, str, list)
