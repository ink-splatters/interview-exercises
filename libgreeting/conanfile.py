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

    default_options = {"shared": False, "fPIC": True}
    generators = "cmake_multi"
    exports_sources = ["src/*", "CMakeLists.txt"]

    settings = {"os": None, "compiler": None, "build_type": None, "arch": None}
    options = {"shared": [True, False], "fPIC": [True, False]}
    requires = (("catch2/2.13.7", "private"),)

    _cmake: CMake = None

    def _get_cmake(self) -> CMake:
        if not self._cmake:
            self._cmake = CMake(self)
        return self._cmake

    def configure(self):
        cmake = self._get_cmake()

        c2opts = self.options["catch2"]

        if self.options["fPIC"]:
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = "ON"
            c2opts.fPIC = "ON"
        c2opts.with_main = True

        cmake.definitions['CATCH_ENABLE_WERROR'] = "ON"
        cmake.configure(build_folder="build")

        return cmake

    def build(self):
        cmake = self._get_cmake()
        cmake.build()

    def package(self):
        self.copy(..., src="src/include", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        # self.cpp_info.
        self.cpp_info.libs = ["libgreeting"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.sharedlinkflags = [] if not "fPIC" in self.options else "-fPIC"
