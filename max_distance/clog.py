from __future__ import annotations
from box import Box


# https://plumbum.readthedocs.io/en/latest/colors.html

def _monkey_patch_ANSIStyle_for_hashing():
    from plumbum.colorlib.styles import ANSIStyle

    ANSIStyle.__hash__ = lambda self: hash(str(self.fg))
    ANSIStyle.__eq__ = lambda self, other: isinstance(other, type(self)) and self.fg == other.fg


_monkey_patch_ANSIStyle_for_hashing()

from plumbum.colorlib import ansicolors as _colors

from cytoolz.dicttoolz import valmap

level = Box(dict(
    info=_colors.fg.LightSkyBlue3A,
    warning=_colors.fg.DarkOrange,
    error=_colors.fg.Red1,
    critical=_colors.fg.Red1 & _colors.bold,
    fatal=_colors.fg.Red3 & _colors.bold))


def cprint(*args, **kw):
    print("⚠", *args, **kw)

def info(*args, **kw):
    cprint("-- ", args, kw)

def warning(*args, **kw):
    cprint("⚠ ", args, kw)


def inf(*args, **kw):
    cprint("⚠ ", args, kw)

def error(*args, **kw):
    cprint("⚠ ", args, kw)


def trace(*args, **kw):
    cprint("➤⚠ ", args, kw)
