from . import __version__
from typing import Optional

from conans.client.conan_api import Conan

from plumbum import cli

from . import clog
from .clog import level as level


class LibGreetingPack(cli.Application):
    """Packs the libgreeting library to conan package"""

    PROGNAME = "LibGreetingPack"
    VERSION = __version__

    def main(self):
        print(level.info & "hi not implemented")


from pathlib import Path
from functools import lru_cache


@lru_cache()
def conan():
    conan, _, _ = Conan.factory()
    return conan


@LibGreetingPack.subcommand("dev-flow")
class Dev(cli.Application):
    """Conan Dev flow"""

    PROGNAME = "Conan Development flow"
    VERSION = __version__

    @cli.positional(cli.ExistingDirectory, cli.ExistingDirectory)
    @cli.switch(["-b", "--build-dir"], argtype=str)
    def main(self, source_dir: str, build_dir: Optional[str] = None):
        clog.trace(level.info, f"conan source {source_dir}")
        conan().source(source_dir)


def run():
    LibGreetingPack.run()
