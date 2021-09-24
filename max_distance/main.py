import beartype
import click
# from beartype import beartype

import typing

from . import log

TimeComplexity = typing.Literal['n^2', 'log', 'linear']

from click_help_colors import *

@click.command(cls=HelpColorsCommand,
               help_headers_color='green',
               help_options_color='magenta',

               )
@click.option('--time',
              type=click.Choice(TimeComplexity.__args__,
                                case_sensitive=False),
                                required=True)
@beartype.beartype
def solve(time: TimeComplexity):
    log.info(f'the chosen cmplexity is:{time}')

# from click oo
# from sortedcollections import SortedSet
#
# def _solution(A):
#     N = len(A)
#     result = 0
#
#
#     for i in range(N):
#         for j in range(N):
#             if A[i] == A[j]:
#                 result = max(result, abs(i - j))
#     return result
#
#
# from typing import Dict, List
#
#
#
# def solution(A):
#     N = len(A)
#     result = 0
#
#
#     # TODO: change to set
#     val_to_idx : Dict[int, SortedSet[int]] = {}
#
#
#     for i in range(N):
#
#         value = A[i]
#         if value not in val_to_idx:
#             val_to_idx[value] = SortedSet()
#
#         val_to_idx[value].add(i)
#
#
#     max_distances = list()
#
#     for k, v in val_to_idx.items():
#         print(f"for {k} idx: {v}")
#
#         last = v.pop()
# #!        if not len(v):
# #            max_distances.append(0)
# #            continue
#
#         first = list(v)[0]
#
#         print(f"f:{first}, l:{last}")
#         max_distances.append(abs(first-last))
#
#
#
#
#     return next(iter(sorted(max_distances, reverse=True)))
#
#
#
# if __name__ == "__main__":
#
#    a = [1,2,3,1,5,1]
#    b=[2,2,2,2,2,2,2,2,2,2]
#
#    print(_solution(a))
#    print(solution(a))
#    print(solution(b))
#
#    l = list()
#    for i in range(0, 50000):
#         l.append(2)
#
#     next()
#     l= [ 2 for x in range(50000) ]
#
#    print(solution(l))
#
