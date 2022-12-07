from typing import Any, Callable, Iterable, Tuple, Union

__all__ = [
    "isfloat",
    "allEqual",
    "allDiff",
    "allNone",
    "anyNone",
    "xor",
    "xand",
    "getNotNone",
    "applyNotNone",
    "flatten",
    "to_ntuple",
    "to_2tuple",
]


def isfloat(x: str) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


################################################################################


def allEqual(*I: Any) -> bool:
    "All items are the same"
    return len(set(I)) == 1


def allDiff(*I: Any) -> bool:
    "All items are different"
    return len(set(I)) == len(I)  # type: ignore


def allNone(*I: Any) -> bool:
    "All items are None"
    return all([x is None for x in I])


def anyNone(*I: Any) -> bool:
    "At least one item is None"
    return any([x is None for x in I])


def xor(arg1: Any, arg2: Any) -> bool:
    "One item is 'not None' and the other is 'None'"
    return not allNone(arg1, arg2) and anyNone(arg1, arg2)


def xand(arg1: Any, arg2: Any) -> bool:
    "Both items are 'not None' or 'None'"
    return allNone(arg1, arg2) or not anyNone(arg1, arg2)


def getNotNone(arg1: Any, arg2: Any) -> Any:
    "return arg1 if arg1 is not None else return arg2"
    return arg1 if arg1 is not None else arg2


def applyNotNone(arg: Any, f: Union[Callable, None] = None) -> Any:
    "return f(arg) if f is not None else return arg"
    return f(arg) if f is not None else arg


################################################################################


def flatten(iterable: Iterable):
    "Flatten an iterable"
    l = []
    for it in iterable:
        if isinstance(it, (list, tuple)):
            l.extend(flatten(it))
        else:
            l.append(it)
    return l


def to_ntuple(item: Any, n: int = 1) -> Tuple[Any]:
    """Converts an item to a tuple of said item of size n

    Args:
        item (Any): Item
        n (int, optional): Number of times to repeat the item. Defaults to 1.

    Returns:
        Tuple[Any]: Tuple of repetead item
    """
    return (item,) * n


to_2tuple = lambda x: to_ntuple(x, 2)


################################################################################

# ENDFILE
