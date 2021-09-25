from plumbum import cli

from . import clog
from . import __version__
from plumbum.colorlib import ansicolors as AC

import plumbum.colors as C

C.use_colors = True
import functools


class MaxDistance(cli.Application):
    DESCRIPTION = AC.fg.Green1 | """Finds maximum distance between equal array elements
    
    The note about performance hint:
    
        0: maximum performance, O(N) [default]
        1: logarithmic performance
        2: O(N^2) performance
    """

    PROGNAME = C.bold & AC.fg.Cyan & "calc-max-distance"
    VERSION = AC.fg.SteelBlue1A & __version__

    COLOR_USAGE = AC.fg.Green1
    COLOR_USAGE_TITLE = C.bold & AC.fg.Green1

    cg_names = ["Meta-switches", "Switches"]
    cg_colors = [AC.DeepSkyBlue1, AC.Green1]
    COLOR_GROUPS = zip(
        cg_names,
        cg_colors
    )

    COLOR_GROUP_TITLES = zip(
        cg_names,
        map(lambda c: C.bold & c, cg_colors))

    def __init__(self, executable):
        super().__init__(executable)
        self.unbind_switches('--help-all')

    @cli.switch(['-p', '--perf-hint'], argtype=int, mandatory=True, help="1\r2\r3\r")
    def perf_hint(self):
        """performance hint to chose the calculation algorithm"""
        # """
        # self._allow_root = True

    def main(self):
        # def cprint(*args, **kw):
        # print("⚠")

        clog.trace("hi not implemented")
        clog.info("hi not implemented")
        clog.warn("hi not implemented")
        clog.error("hi not implemented")
        clog.fatal("hi not implemented")


def run():
    MaxDistance.run()
# import beartype
# import click
# # from beartype import beartype
#
# import typing
#
# from . import log
# from . import solution
# from . import utils
#
# TimeComplexity = typing.Literal['n^2', 'log', 'linear']
# InputGenType = typing.Literal['random', 'equal', 'modulo']
#
# from click_help_colors import *
#
# import click
# import ast
#
#
# # https://stackoverflow.com/questions/47631914/how-to-pass-several-list-of-arguments-to-click-option/47730333
# class PythonLiteralOption(click.Option):
#
#     def type_cast_value(self, ctx, value):
#         try:
#             return ast.literal_eval(value)
#         except:
#             raise click.BadParameter(value)
#
#
# def cb_gen_type(ctx, _, value):
#     print(str(ctx))
#     if not 'gen_size' in ctx.params:
#         raise click.UsageError('--gen-size must be specified')
#
#     return value
#
#
# @click.command(cls=HelpColorsCommand,
#                help_headers_color='green',
#                help_options_color='magenta',
#
#                )
# @click.option('--time',
#               type=click.Choice(TimeComplexity.__args__,
#                                 case_sensitive=False),
#               required=True)
# @click.option('--gen-type',
#               type=click.Choice(InputGenType.__args__,
#                                 case_sensitive=False), is_eager=True, callback=cb_gen_type, default='linear')
# @click.option('--gen-size', type=int)
# @click.option('--gen-param', type=int)
# @click.option('--input', cls=PythonLiteralOption, default=[])
# @click.pass_context
# # @beartype.beartype
# def solve(ctx, time: TimeComplexity, gen_type: typing.Optional[InputGenType],
#           gen_size: typing.Optional[int],
#           gen_param: typing.Optional[int],
#           input: typing.Optional[list[int]]):
#     """
#     Finds maximum distance between equal array elements
#
#     TIME specifies expected time complexity: O(n^2), O(log), O(N)
#
#     GEN-TYPE specifies the input data generation strategy
#
#     INPUT: if GEN-TYPE is not set, it's treated as integer array,
#           otherwise it's the length of the generated array
#     Examples:
#
#
#     """
#     log.info(f'the chosen complexity is:{time}')
#     input_str = f'{input}' if not gen_type else f'generated: type={gen_type}; size={gen_size}'
#     log.info(f'the input is: {input_str}')
#
#     input = input if input or utils.gen_input()
#
#     solution.Square
#     switch_gen_type = {
#         'n^2': lambda : solution.Square.solve()
#     }
#
#
# #
# #
# # def solution(A):
# #     N = len(A)
# #     result = 0
# #
# #
# #     # TODO: change to set
# #     val_to_idx : Dict[int, SortedSet[int]] = {}
# #
# #
# #     for i in range(N):
# #
# #         value = A[i]
# #         if value not in val_to_idx:
# #             val_to_idx[value] = SortedSet()
# #
# #         val_to_idx[value].add(i)
# #
# #
# #     max_distances = list()
# #
# #     for k, v in val_to_idx.items():
# #         print(f"for {k} idx: {v}")
# #
# #         last = v.pop()
# # #!        if not len(v):
# # #            max_distances.append(0)
# # #            continue
# #
# #         first = list(v)[0]
# #
# #         print(f"f:{first}, l:{last}")
# #         max_distances.append(abs(first-last))
# #
# #
# #
# #
# #     return next(iter(sorted(max_distances, reverse=True)))
# #
# #
# #
# # if __name__ == "__main__":
# #
# #    a = [1,2,3,1,5,1]
# #    b=[2,2,2,2,2,2,2,2,2,2]
# #
# #    print(_solution(a))
# #    print(solution(a))
# #    print(solution(b))
# #
# #    l = list()
# #    for i in range(0, 50000):
# #         l.append(2)
# #
# #     next()
# #     l= [ 2 for x in range(50000) ]
# #
# #    print(solution(l))
# #
