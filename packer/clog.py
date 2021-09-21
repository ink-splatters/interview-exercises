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

level = valmap(lambda v: v.stdout, Box(dict(
    info=_colors.fg.LightSkyBlue3A,
    warn=_colors.fg.DarkOrange,
    err=_colors.fg.Red1,
    critical=_colors.fg.Red1 & _colors.bold,
    fatal=_colors.fg.Red3 & _colors.bold),
    frozen_box=True
))


def cprint(*args, **kw):
    print(*args, **kw)


def trace(*args, **kw):
    cprint("➤ ", args, kw)
