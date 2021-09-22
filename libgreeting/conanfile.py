#!/usr/bin/env python
import conans
import typing


class CMake(conans.CMake):
    def __init__(self, conanfile,
                 generator="Ninja",
                 make_program="ninja",
                 set_cmake_flags=True,
                 **kw):
        self.conan = conanfile
        super().__init__(conanfile,
                         generator=generator,
                         make_program=make_program,
                         set_cmake_flags=set_cmake_flags,
                         **kw)

    def configure(self, *args, **kw):
        self.definitions["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        self.conan.options["catch2:fPIC"] = self.conan.options.fPIC
        if self.conan.settings.os in ("Macos", "iOS", "watchOS", "tvOS"):
            self.conan.settings.compiler.libcxx = "libc++"
            self.definitions['CATCH_ENABLE_WERROR'] = "ON"

        return super().configure(*args, **kw)


class Greeting(conans.ConanFile):
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

    options = {"shared": [True, False], "fPIC": [True, False], "build_type": ["Release", "Debug"]}
    default_options = {"shared": False, "fPIC": True, "build_type": "Release", "catch2:with_main": True}

    requires = "catch2/2.13.7"

    def _configure_and_build(self):
        cmake = CMake(self)

        cmake.configure()
        cmake.build()
        cmake.test()

        return cmake

    def build(self):
        self._configure_and_build()

    def package(self):
        cmake = self._configure_and_build()
        cmake.install()

    def package_info(self):
        # self.cpp_info.
        self.cpp_info.libs = ["greeting"]
        self.cpp_info.includedirs = ["include"]
