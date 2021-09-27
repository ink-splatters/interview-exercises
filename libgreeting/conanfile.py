#!/usr/bin/env python
from conans import ConanFile, CMake
import typing


class Greeting(ConanFile):
    name = "greeting"
    version = "0.1.0"
    author = "Peter A. <ink.splatters@pm.me>"
    topics = ("conan-boilerplate", "cpp-boilerplate", "conan-cpp", "conan-cmake")
    license = "MIT"
    url = "https://github.com/ink-splatters/interview-exercises.git"
    description = """Toy Conan package to demonstrate conan/cmake integration based
                     on simple library exposing API which is tested using catch2
                  """

    generators = "cmake"
    # exports_sources = ["src/**", "tests/**", "include/**", "CMakeLists.txt"]
    exports_sources = ["src", "include", "CMakeLists", "conanfile.py"]

    settings = {"os": None, "build_type": None, "arch": None, "compiler": None}

    build_requires = "cmake/[>=3.21], ninja[>=1.10], catch2/2.13.7"

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True, "catch2:with_main": True}

    _cmake = None

    def _get_or_conf_cmake(self):
        if not self._cmake:
            self._cmake = CMake(
                self,
                generator="Ninja",
                make_program="ninja",
                set_cmake_flags=True
            )

        self.settings.build_type = self.settings.get_safe("build_type", default="Release")

        self._cmake.definitions['CATCH_ENABLE_WERROR'] = "ON"
        self.options["catch2"].fPIC = self.options.fPIC
        self.options["catch2"].with_main = True

        self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._get_or_conf_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._get_or_conf_cmake()
        cmake.install()

    def package_info(self):
        pass
        # self.cpp_info.
        # self.cpp_info.libs = ["greeting"]
        # self.cpp_info.includedirs = ["include"]
