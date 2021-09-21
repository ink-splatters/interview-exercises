#!/usr/bin/env python
from conans import ConanFile, CMake


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
    exports_sources = ["src/**", "CMakeLists.txt"]

    settings = {"os": None, "build_type": None, "arch": None, "compiler": None}

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    requires = (("catch2/2.13.7", "private"),)

    def _configure_and_build(self):
        if self.settings.os in ("Macos", "iOS", "watchOS", "tvOS"):
            self.settings.compiler.libcxx="libc++"

        self.settings.compiler.cppstd="gnu17"

        cmake = CMake(self, generator="Ninja",
                      make_program="ninja",
                      set_cmake_flags=True)

        c2opts = self.options["catch2"]

        self.options["catch2"].fPIC= self.options.fPIC
        self.options["catch2"].with_main = True
        cmake.definitions['CATCH_ENABLE_WERROR'] = True

        if self.settings.compiler == 'Visual Studio':
            del self.options.fPIC

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
