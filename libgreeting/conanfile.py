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
    exports_sources = ["src/**", "tests/**", "include/**", "CMakeLists.txt"]

    settings = {"os": None, "build_type": None, "arch": None, "compiler": None}

    requires = "catch2/2.13.7"

    options = {"shared": [True, False], "fPIC": [True, False], "build_type": ["Release", "Debug"]}
    default_options = {"shared": False, "fPIC": True, "catch2:with_main": True, "build_type": "Release"}

    _cmake = None



    def _cmake_configure(self):
        cmake = self._cmake
        if not cmake:
            cmake = CMake(
                self,
                generator="Ninja",
                make_program="ninja",
                set_cmake_flags=True
            )
            self._cmake = cmake

        cmake.definitions["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        cmake.definitions['CATCH_ENABLE_WERROR'] = "ON"
        self.options["catch2"].fPIC = self.options.fPIC
        self.options["catch2"].with_main = True

        print(f"the os is: {self.settings.os}")
        if self.settings.os in ("Macos", "iOS", "watchOS", "tvOS"):
            self.settings.compiler.libcxx = "libc++"

        cmake.configure()
        return cmake

    def build(self):
        cmake = self._cmake_configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._cmake_configure()
        cmake.install()

    def package_info(self):
        # self.cpp_info.
        self.cpp_info.libs = ["greeting"]
        self.cpp_info.includedirs = ["include"]
