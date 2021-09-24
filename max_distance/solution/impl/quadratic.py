from .. import Solution


class NxNSolution(Solution):

    @abstrac
    def solution():
        N = len(A)
        result = 0

        for i in range(N):
            for j in range(N):
                if A[i] == A[j]:
                    result = max(result, abs(i - j))
        return result
