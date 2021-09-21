from __future__ import annotations

from . import __version__
from typing import Optional
from conans.client.conan_api import Conan
from plumbum import cli

from box import Box

# https://plumbum.readthedocs.io/en/latest/colors.html

def __monkey_patch_ANSIStyle_for_hashing():
    from plumbum.colorlib.styles import ANSIStyle

    ANSIStyle.__hash__ = lambda self: hash(str(self.fg))
    ANSIStyle.__eq__ = lambda self, other: isinstance(other, type(self)) and  self.fg == other.fg

__monkey_patch_ANSIStyle_for_hashing()

from plumbum.colorlib import ansicolors as colors

level = Box(dict(
    info=colors.fg.LightSkyBlue3A,
    warn=colors.fg.DarkOrange,
    err=colors.fg.Red1,
    critical=colors.fg.Red1 & colors.bold,
    fatal=colors.fg.Red3 & colors.bold),
    frozen_box=True
)


def clog(*args, **kw):
    print(*args, **kw)


def trace(*args, **kw):
    clog(f"➤ {args}{kw}")
