import string
from typing import Any, Callable, Dict, List, Tuple, Union

from tqdm import tqdm

from .assertions import assert_types
from .common import applyNotNone

__all__ = [
    "tprint",
    "print_",
    "trunc",
    "indent",
    "d2s",
    "ssplit",
    "remove_char",
    "sep_letters",
    "sep_numbers",
    "sep_punctuation",
    "sep_letters_numbers",
    "sep_letters_punctuation",
    "sep_numbers_punctuation",
    "str2int_list",
]


def tprint(s: str):
    """Prints with tqdm"""
    tqdm.write(s)


def print_(*args: Any, yes: bool = True, **kwargs: Any) -> None:
    """Conditional printing

    Args:
        yes (bool, optional): If False does not print. Defaults to True.
    """
    if not yes:
        return
    print(*args, **kwargs)


def trunc(msg: str, length: int = 1e3):  # type:ignore
    "Truncates a string and adds [...] if len(msg) > lenght"
    if length < 1:
        raise ValueError(
            "Truncation length must be greater than zero. Got: {}".format(length)
        )
    length = int(length)

    if len(msg) <= length:
        return msg

    return msg[: max(length, length - 5)] + "[...]"


def indent(s: str, spaces: int = 2, start: Union[str, None] = None, **kwargs) -> str:
    """Indents a string

    Args:
        s (str): String to indent
        spaces (int, optional): Number of indent spaces. Defaults to 2.
        start (str, optional): String start. Defaults to None.

    Returns:
        str: Indented string
    """
    sp = "\n" + spaces * " "
    return (spaces * " " if start is None else start) + sp.join(s.split("\n"))


def d2s(d: Dict[Any, Any], spaces: int = 2, lvl: int = 0) -> str:
    """Converts a dictionary to a string

    Args:
        d (Dict[Any, Any]): Dictionary
        spaces (int, optional): Number of indentation spaces. Defaults to 2.
        lvl (int, optional): Indentation level. Defaults to 0.

    Returns:
        str: pretty dictionary as a string

    """

    str_ = ""
    for k, v in d.items():
        if isinstance(v, dict):
            str_ += f"{lvl*spaces*' '}{k}: \n{d2s(v, spaces, lvl+1)}"
        else:
            str_ += f"{lvl*spaces*' '}{k}: {v}\n"
    return str_


def ssplit(
    str_: str,
    seps: Union[str, List[str]],
    map_func: Union[Callable, None] = None,
) -> List[str]:
    """Splits a string based on separators

    Note:
        Removes empty strings after spliting

    Args:
        str_ (str): String to split
        seps (Union[str, List[str]]): List of string separators
        map_func (Union[Callable, None], optional): Mapping function to each
        separated string . Defaults to None.

    Returns:
        List[str]: List of strings split with separators

    """
    assert_types(str_, str)
    assert_types(seps, str, list, tuple)

    def remove_empty_str(str_: str, sep: str):
        return list(filter(lambda x: x != "", str_.split(sep)))

    if len(seps) < 1:  # No seps, return original str
        return [str_]
    if len(seps) == 1:
        out = remove_empty_str(str_, seps[0])

        return applyNotNone(out, map_func)

    old_sep = seps[0]
    for sep in seps:
        str_ = str_.replace(old_sep, sep)
        old_sep = sep

    out = remove_empty_str(str_, old_sep)

    return applyNotNone(out, map_func)


def remove_char(str_: str, char: str) -> str:
    """Removes a character from a string

    Args:
        str_ (str): String
        char (str): String character

    Returns:
        str: String without the character

    """
    return "".join(ssplit(str_, char))


sep_letters = string.ascii_letters
sep_numbers = string.digits
sep_punctuation = string.punctuation
sep_letters_numbers = sep_numbers + sep_letters
sep_letters_punctuation = sep_letters + sep_punctuation
sep_numbers_punctuation = sep_numbers + sep_punctuation

str2int_list = lambda x: [int(x_) for x_ in x]


def format_power(size: Union[int, float], power=1024) -> Tuple[Union[int, float], str]:
    # TODO: Clean, add to __all__
    n = 0
    power_labels = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size >= power:
        size /= power
        n += 1
        if n not in power_labels:
            raise ValueError(f"Invalid label for {size}.")
    return size, power_labels[n] + ("B" if power == 1024 else "")


# ENDFILE
