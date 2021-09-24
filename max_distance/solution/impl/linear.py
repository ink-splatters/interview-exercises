import abc
from typing import Iterable
from beartype import beartype


class Linear(metaclass=abc.ABC):  # or https://zopeinterface.readthedocs.io/en/latest/README.html
    """
    Interface solution classes should implement
    """

    # list is used b
    @staticmethod
    @abc.abstractmethod
    @beartype
    def solve(data: Iterable[int]):


        pass
