cmake_minimum_required(VERSION 3.14)

project(interviw-excersizes)

# Download automatically, you can also just copy the conan.cmake file
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
            "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run(REQUIRES Catch2/2.6.0@catchorg/stable
        BASIC_SETUP)

#
#include(ProcessorCount)
#ProcessorCount(N)
#
#if(NOT N EQUAL 0)
#    set(CTEST_BUILD_FLAGS -j${N})
#    set(ctest_test_args ${ctest_test_args} PARALLEL_LEVEL ${N})
#endif()
#
## TODO: review and/or add
## TODO Refactor according to Jason's approach https://www.youtube.com/watch?v=YbgH7yat-Jo
## catch2/2.11.0
## docopt.cpp/0.6.2
## fmt/6.2.0
## spdlog/1.5.0
#
##if (WIN32)
##    # TODO
##else()
##    conan_cmake_run(CONANFILE conanfile.txt
##            BASIC_SETUP CMAKE_TARGETS KEEP_RPATHS
##            GENERATOR    ${CMAKE_GENERATOR}
##            BUILD       missing
##            SETTINGS    compiler.cppstd=20
##            compiler.libcxx=libc++
##            build_type=${CMAKE_BUILD_TYPE}
##            ENV          CONAN_CPU_COUNT=${N}
##            )
##endif ()
##
#if (APPLE)
#    set(CMAKE_INSTALL_RPATH "@executable_path/../lib")
#else()
#    set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib:$ORIGIN")
#endif()
##
##set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
##

add_compile_options("-Wextra" "-Werror" "$<$<CONFIG:RELEASE>:-O3>" "-stdlib=libc++")
add_link_options("-stdlib=libc++" "-lc++abi")
##
##add_subdirectory(src/common)
##add_subdirectory(src/exampleapp)

add_subdirectory(libgreeting)
add_subdirectory(app)