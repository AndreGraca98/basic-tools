import sys

sys.path.append("../basic-tools")

import unittest

from basic_tools.common import *


class Test_isfloat(unittest.TestCase):
    def test_isfloat_is_a_float(self):
        number = "2.3"
        assert isfloat(number), f"number={number} is not a float"

    def test_isfloat_is_a_float_exp_number(self):
        number = "2e3"
        assert isfloat(number), f"number={number} is not a float"

    def test_isfloat_is_a_float_no_dots(self):
        number = "234"
        assert isfloat(number), f"number={number} is not a float"

    def test_isfloat_is_not_a_float_multiple_dots(self):
        number = "2.3.4"
        assert not isfloat(number), f"number={number} is not a float"

    def test_isfloat_is_not_a_float_letters(self):
        number = "2.asd"
        assert not isfloat(number), f"number={number} is not a float"


class Test_allEqual(unittest.TestCase):
    def test_allEqual_all_items_are_equal(self):
        a = 1
        b = 1
        c = 1
        assert allEqual(
            a, b, c
        ), f"Not all arguments are equal. Got: a={a}, b={b}, c={c}"

    def test_allEqual_some_items_are_different(self):
        a = 1
        b = 2
        c = 3
        assert not allEqual(
            a, b, c
        ), f"Not all arguments are equal. Got: a={a}, b={b}, c={c}"


class Test_allDiff(unittest.TestCase):
    def test_allDiff_all_items_are_different(self):
        a = 1
        b = 2
        c = 3
        assert allDiff(
            a, b, c
        ), f"Not all arguments are different. Got: a={a}, b={b}, c={c}"

    def test_allDiff_some_items_are_equal(self):
        a = 1
        b = 1
        c = 3
        assert not allDiff(
            a, b, c
        ), f"Not all arguments are different. Got: a={a}, b={b}, c={c}"


class Test_allNone(unittest.TestCase):
    def test_allNone_all_items_are_None(self):
        a = None
        b = None
        c = None
        assert allNone(a, b, c), f"Not all arguments are None. Got: a={a}, b={b}, c={c}"

    def test_allNone_some_items_are_not_None(self):
        a = None
        b = 2
        c = 3
        assert not allNone(
            a, b, c
        ), f"Not all arguments are None. Got: a={a}, b={b}, c={c}"

    def test_allNone_all_items_are_not_None(self):
        a = 1
        b = 2
        c = 3
        assert not allNone(
            a, b, c
        ), f"Not all arguments are None. Got: a={a}, b={b}, c={c}"


class Test_anyNone(unittest.TestCase):
    def test_anyNone_some_items_are_None(self):
        a = 1
        b = 2
        c = None
        assert anyNone(a, b, c), f"Not all arguments are None. Got: a={a}, b={b}, c={c}"

    def test_anyNone_all_items_are_None(self):
        a = None
        b = None
        c = None
        assert anyNone(a, b, c), f"Not all arguments are None. Got: a={a}, b={b}, c={c}"

    def test_anyNone_all_items_are_not_None(self):
        a = 1
        b = 1
        c = 3
        assert not anyNone(
            a, b, c
        ), f"Not all arguments are None. Got: a={a}, b={b}, c={c}"


class Test_xor(unittest.TestCase):
    def test_xor_val_none(self):
        a = 1
        b = None
        assert xor(
            a, b
        ), f"One of the items must be 'None' and the other 'not None'. Got: a={a}, b={b}"

    def test_xor_val_val(self):
        a = 1
        b = 1
        assert not xor(
            a, b
        ), f"One of the items must be 'None' and the other 'not None'. Got: a={a}, b={b}"

    def test_xor_none_none(self):
        a = None
        b = None
        assert not xor(
            a, b
        ), f"One of the items must be 'None' and the other 'not None'. Got: a={a}, b={b}"


class Test_xand(unittest.TestCase):
    def test_xand_val_none(self):
        a = 1
        b = None
        assert not xand(
            a, b
        ), f"Both items are should be 'not None' or 'None'. Got: a={a}, b={b}"

    def test_xand_val_val(self):
        a = 1
        b = 1
        assert xand(
            a, b
        ), f"Both items are should be 'not None' or 'None'. Got: a={a}, b={b}"

    def test_xand_none_none(self):
        a = None
        b = None
        assert xand(
            a, b
        ), f"Both items are should be 'not None' or 'None'. Got: a={a}, b={b}"


class Test_getNotNone(unittest.TestCase):
    def test_getNotNone_both_args_are_not_None(self):
        a = 1
        b = 2
        c = getNotNone(a, b)
        assert a == c

    def test_getNotNone_both_args_are_None(self):
        a = None
        b = None
        c = getNotNone(a, b)
        assert a == b == c

    def test_getNotNone_first_arg_is_not_None(self):
        a = 1
        b = None
        c = getNotNone(a, b)
        assert a == c

    def test_getNotNone_first_arg_is_None_second_arg_is_not_None(self):
        a = None
        b = 1
        c = getNotNone(a, b)
        assert b == c


#
# applyNotNone
