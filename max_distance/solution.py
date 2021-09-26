import multimethod as MM

from .perf_hint import *


@MM.multimethod
def solve(perf_hint: PerfHint):
    raise NotImplementedError("not implemented")


@solve.register(Square)
def solve_NxN():
    print('Square')


@solve.register(Log)
def solve_logarithmic():
    print('Log, that is better')


@solve.register(Linear)
def solve_linear():
    print('Wow')
