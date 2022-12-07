__all__ = [
    "ClassExistsError",
    "EmptyDirectoryError",
]


class ClassExistsError(Exception):
    """A class with the same name already exists"""


class EmptyDirectoryError(Exception):
    """The directory is empty"""


# ENDFILE
