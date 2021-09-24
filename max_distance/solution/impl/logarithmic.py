import abc
import beartype
import typing
from .. import Solution


class Logarithmic(Solution):  # or https://zopeinterface.readthedocs.io/en/latest/README.html
    """
    Interface solution classes should implement
    """

    @staticmethod
    @beartype.beartype
    def solve(data: typing.Iterable[int]) -> int:
        pass
