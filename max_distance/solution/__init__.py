import abc
import beartype
import typing

class Solution(metaclass=abc.ABC):  # or https://zopeinterface.readthedocs.io/en/latest/README.html
    """
    Interface solution classes should implement
    """

    @staticmethod
    @abc.abstractmethod
    @beartype.beartype
    def solve(data: typing.Iterable[int]) -> int:
        pass


from .impl.linear import *
from .impl.square import *
from .impl.logarithmic import *