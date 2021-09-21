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
    generators = "cmake"
    exports_sources = ["src/*", "CMakeLists.txt"]

    settings = {"os": None, "build_type": None, "arch": None, "compiler": None }

    options = {"shared": [True, False], "fPIC": [True, False]}
    requires = (("catch2/2.13.7", "private"),)

    _cmake = None

    def _get_or_cfg_cmake(self):
        if self._cmake:
            return self._cmake
        cmake = CMake(self)
            # , generator="Ninja",
            #           # make_program="ninja",
            #           parallel=True,
            #           set_cmake_flags=True)
        self._cmake = cmake

        # c2opts = self.options["catch2"]
        #
        # cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options["fPIC"]
        # c2opts.fPIC = self.options["fPIC"]
        # c2opts.with_main = True
        #
        # cmake.definitions['CATCH_ENABLE_WERROR'] = True
        #
        # # Mitigate "clang: warning: include path for libstdc++ headers not found; pass '-stdlib=libc++' on the command line to
        # # use the libc++ standard library instead [-Wstdlibcxx-not-found]"
        # if self.settings["os"] in ("Macos", "iOS", "watchOS", "tvOS"):
        #     self.settings.compiler.libcxx="libc++"
        #
        return self._cmake

    def configure(self):


    def build(self):
        cmake = CMake(self)
        # self.settings.compiler.cppstd="20"
        #
        # cmake = self._get_or_cfg_cmake()
        cmake.configure()
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
        self.cpp_info.libs = ["catch2", "greeting"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.sharedlinkflags = [] if not "fPIC" in self.options else "-fPIC"
