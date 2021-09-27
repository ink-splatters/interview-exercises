# import multimethod as MM
#
# from .perf_hint import *
#
#
# @MM.multimethod
# def solve(perf_hint: PerfHint):
#     raise NotImplementedError("not implemented")
#
#
# @solve.register(Square)
# def solve_NxN():
#     print('Square')
#
#
# @solve.register(Log)
# def solve_logarithmic():
#     print('Log, that is better')
#
#
# # @solve.register(Linear)


from typing import List, Dict


def solve(A: List[int]) -> int:
    d: Dict[int, int] = {}  # element -> index

    max_distance = 0
    for i, x in enumerate(A):
        if not x in d:
            d[x] = i
        else:
            max_distance = max(max_distance, abs(i - d[x]))

    return max_distance


print(solve([1, 2, 3, 5, 1, 2]))
print(solve([1, 1, 1, 1, 1, 1, 1]))
print(solve([]))
print(solve([1, 2, 3]))
print(solve([1, 2, 3, 4]))

# for x, y in enumerate(A[0:mid]), enumerate(reversed(A[mid:])):
#     print((x, y))
