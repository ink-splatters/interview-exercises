import abc
from typing import Iterable, Union, List
from beartype import beartype


class Solution(metaclass=abc.ABC):  # or https://zopeinterface.readthedocs.io/en/latest/README.html
    """
    Interface solution classes should implement
    """

    @beartype
    @staticmethod
    @abc.abstractmethod
    def solve(data: Union[List[int], Iterable[int]]):
        pass
