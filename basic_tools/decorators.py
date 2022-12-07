import time
from datetime import timedelta
from functools import partial
from typing import Callable

__all__ = [
    "nothing_decorator",
    "conditional_decorator",
    "timer",
    "doc_printer",
    "conditional_error_notification_decorator",
    "email_notification",
]


def nothing_decorator(function, **_):
    def _nothing_decorator(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return _nothing_decorator


def conditional_decorator(condition: bool, decorator: Callable, *args, **kwargs):
    """Wrapper for conditional decorating. If <condition> == True , the
    <function> will be decorated with <decorator>

    Usage:
        @conditional_decorator(condition=True, decorator=timer,  *args,
        **kwargs)\n \t def some_function(): \n \t \t ...


    Args:
        condition (bool): Condition
        decorator (Callable): Inner decorator
    """

    def _conditional_decorator(function):
        return decorator(function, *args, **kwargs) if condition else function

    return _conditional_decorator


def timer(function: Callable, timer_str: str = "Timer finished"):
    """Decorator to time some function

    Args:
        function (Callable): Function
        timer_str (str, optional): Timer description. Defaults to "Timer finished".
    """

    def _timer(*args, **kwargs):
        start = time.perf_counter_ns()
        result = function(*args, **kwargs)
        end = time.perf_counter_ns()

        t = timedelta(microseconds=(end - start) / 1e3)
        print(f"{timer_str} » Total: {t}")

        return result

    return _timer


def doc_printer(function: Callable):
    """Prints a function docstring

    Args:
        function (Callable): Function
    """

    def _doc_printer(*args, **kwargs):
        print(
            f"{'=' * 80}\nFunction <{function.__name__}> docstring:\n{function.__doc__}\n{'=' * 80}"
        )
        result = function(*args, **kwargs)
        return result

    return _doc_printer


# TRY IMPORT EMAIL-TOOLS
try:
    from email_tools import Email, email_notification_wrapper  # type:ignore

    conditional_error_notification_decorator = partial(
        conditional_decorator, decorator=email_notification_wrapper
    )
    email_notification = lambda *args, **kwargs: Email().send(*args, **kwargs)
except ImportError:
    print(
        f"Package: email-tools not installed ! Use < pip install git+https://github.com/AndreGraca98/email-tools.git > to install package"
    )
    conditional_error_notification_decorator = partial(
        conditional_decorator, decorator=nothing_decorator
    )
    email_notification = lambda *args, **kwargs: None


# ENDFILE
