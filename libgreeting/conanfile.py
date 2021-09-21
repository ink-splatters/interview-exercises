#!/usr/bin/env python3
from conans import ConanFile, CMake

# required_conan_version = ">=1.33.0" # CMakeDeps


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
    settings = {"os": None, "compiler": None, "build_type": None, "arch": ["x86_64"]}
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = ["src/*", "CMakeLists.txt"]

    def requirements(self):
        self.requires("catch2/2.13.7")

    def configure(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options["fPIC"]

        cmake.configure(build_folder="build")
        return cmake


def build(self):
    cmake = CMake(self)
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
    self.cpp_info.sharedlinkflags = [] if not "fPIC" in self.options else self.options.fPIC
