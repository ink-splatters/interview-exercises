from .. import Solution

import typing
import beartype


class Square(Solution):
    @staticmethod
    @beartype.beartype
    def array_solve(A: list[int]) -> int:

        N = len(A)
        result = 0

        for i in range(N):
            for j in range(N):
                if A[i] == A[j]:
                    result = max(result, abs(i - j))
        return result
