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
        self._set_cxx_flags()
        self._set_cmake_export()
        self._set_catch2_opts()
        self._set_cmake_export()
        self._set_libcxx()

        super().configure(*args, **kw)

    def _set_cxx_flags(self):
        key = "CONAN_CXX_FLAGS"
        lcxxflags: typing.List[str] = self.definitions.get(key).split() + ["-Werror", "-Wextra"]
        self.definitions[key] = " ".join(lcxxflags)
        print(f"lcxx: {lcxxflags}")

    def _set_cmake_export(self):
        self.definitions["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"

    def _set_libcxx(self):
        if self.conan.settings.os in ("Macos", "iOS", "watchOS", "tvOS"):
            self.conan.settings.compiler.libcxx = "libc++"

    def _set_catch2_opts(self):
        self.conan.options["catch2"].fPIC = self.conan.options.fPIC
        self.conan.options["catch2"].with_main = True
        self.definitions['CATCH_ENABLE_WERROR'] = True


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
    exports_sources = ["src/**", "CMakeLists.txt"]

    settings = {"os": None, "build_type": None, "arch": None, "compiler": None}

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    requires = (("catch2/2.13.7", "private"),)

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
