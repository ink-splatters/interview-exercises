from __future__ import annotations
import box
import beartype

from plumbum.colorlib import ansicolors as _colors, styles

_c = _colors.fg
style = box.Box(dict(
    trace=_c.SteelBlue1A,
    info=_c.Green1,
    warn=_c.DarkOrange,
    error=_c.LightRed,
    fatal=_c.Red1 & _colors.bold))


@beartype.beartype
def cprint(style: styles.ANSIStyle, msg: str):
    print(style & msg)


def info(msg: str):
    cprint(style.info, f"{msg}")


def warn(msg: str):
    cprint(style.warn, f"WARNING: {msg}")


def error(msg: str):
    cprint(style.error, f"ERROR: {msg}")

def fatal(msg: str):
    cprint(style.fatal, f"FATAL: {msg}")


def trace(msg: str):
    cprint(style.trace, f"➤ {msg}")
