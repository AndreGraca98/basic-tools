from typing import Any, Union

from varname import argname

from .common import flatten, xor

__all__ = ["assert_xor", "assert_range", "assert_types"]


def assert_xor(arg1: Any, arg2: Any) -> None:
    """

    Args:
        arg1 (Any): Value 1
        arg2 (Any): Value 2

    Raises:
        ValueError: Raises error if none of the arguments is 'None' or if both are 'None'
    """
    if xor(arg1, arg2):
        return

    raise ValueError(
        f"One of the items must be 'None' and the other 'not None': {argname('arg1', vars_only=True)}={arg1}, {argname('arg2', vars_only=True)}={arg2}"
    )


def assert_range(
    value: Union[int, float], m: Union[int, float], M: Union[int, float]
) -> None:
    """

    Args:
        value (Union[int, float]): Value
        m (Union[int, float]): Minimum
        M (Union[int, float]): Maximum

    Raises:
        ValueError: Raises error if value is outside [m, M]
    """
    if m <= value <= M:
        return

    raise ValueError(
        f"Expected {m} < {argname('value', vars_only=True)} < {M} . Got:  {argname('value', vars_only=True)} = {value}"
    )


def assert_types(value: Any, *types: type) -> None:
    """

    Args:
        value (Any): Value

    Raises:
        ValueError: Raises error if there is not at least one type
        TypeError: Raises error if value is not of one of provided types
    """
    if not types:
        raise ValueError("Expected at least one type")

    ntypes = flatten(types)

    if isinstance(value, tuple(ntypes)):
        return

    raise TypeError(
        f"Expected type: {list(map(lambda x:x.__name__, set(ntypes)))}. Got: type({argname('value', vars_only=True)})={type(value).__name__}"
    )


# ENDFILE
