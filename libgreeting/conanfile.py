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

    def _configure_cmake(self):
        cmake = CMake(self, generator="Ninja",
                      make_program="ninja",

                      parallel=True,
                      set_cmake_flags=True)

        c2opts = self.options["catch2"]

        if self.options.fPIC:
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = "ON"
        c2opts.fPIC = self.options.fPIC
        c2opts.with_main = True
        cmake.definitions['CATCH_ENABLE_WERROR'] = True

        cmake.configure()

        return cmake

    def build(self):
        if self.settings.compiler == 'Visual Studio':
            del self.options.fPIC

        cmake = self._configure_cmake()
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        # self.cpp_info.
        self.cpp_info.libs = ["greeting"]
        self.cpp_info.includedirs = ["include"]
