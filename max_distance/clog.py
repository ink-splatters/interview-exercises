from __future__ import annotations
import box as b
import beartype as bt
import typing as T

T.SupportsInt
from plumbum.colorlib import ansicolors as _colors, styles

_c = _colors.fg
style = b.Box(dict(
    trace=_c.SteelBlue1A,
    info=_c.Green1,
    warn=_c.DarkOrange,
    error=_c.LightRed,
    fatal=_c.Red1 & _colors.bold))


@bt.beartype
def cprint(style: styles.ANSIStyle, msg: str):
    print(style & msg)


def info(input: T.Any):
    cprint(style.info, f"{str(input)}")


def warn(input: T.Any):
    cprint(style.warn, f"WARNING: {str(input)}")


def error(input: T.Any):
    cprint(style.error, f"ERROR: {str(input)}")


def fatal(input: T.Any):
    cprint(style.fatal, f"FATAL: {str(input)}")


def trace(input: T.Any):
    cprint(style.trace, f"➤ {str(input)}")
