from enum import Enum

__all__ = ["CallableEnum"]


class CallableEnum(Enum):
    """A class to inherit from to allow the usage of classes as values."""

    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)

    @classmethod
    def keys(cls):
        return set(cls._member_map_.keys())


# ENDFILE
