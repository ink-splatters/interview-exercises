import multimethod as MM
import typing as T

NxN = T.Literal['nxn', '0']
Log = T.Literal['log', '1']
Linear = T.Literal['linear', 'max', '2']

PerfHint = T.Literal[NxN, Log, Linear]


@MM.multimethod
def solve(perf_hint: PerfHint):
    raise NotImplementedError("not implemented")


@solve.register(NxN)
def _(perf_hint: NxN):
    print('NxN')


@solve.register(Log)
def _(perf_hint: Log):
    print('Log, that is better')


@solve.register(Linear)
def _(perf_hint: Linear):
    print('Wow')


# class PerfHint(Enum):
#     Sq
# >>> class Color(Enum):
# ...     RED = 1
# ...     GREEN = 2
# ...     BLUE = 3

# @beartype.beartype
@decorator.dispatch_on('perf_hint')
def solve(perf_hint):
    raise NotImplementedError("not implemented")


@solve.register(typing.Literal['max'])
def linearSolve(perf_hint):
    pass
