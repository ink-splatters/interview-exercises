cmake_minimum_required(VERSION 3.21)

project(greeting LANGUAGES CXX)

message(${CMAKE_BINARY_DIR})
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

# https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_generator.html#targets-approach
conan_basic_setup(TARGETS)

# actually to suppress the warnings...
message(STATUS "CATCH_ENABLE_WERROR ${CATCH_ENABLE_WERROR}")
message(STATUS "CMAKE_EXPORT_NO_PACKAGE_REGISTRY ${CMAKE_EXPORT_NO_PACKAGE_REGISTRY}")
message(STATUS "CMAKE_INSTALL_BINDIR ${CMAKE_INSTALL_BINDIR}")
message(STATUS "CMAKE_INSTALL_DATAROOTDIR ${CMAKE_INSTALL_DATAROOTDIR}")
message(STATUS "CMAKE_INSTALL_INCLUDEDIR ${CMAKE_INSTALL_INCLUDEDIR}")
message(STATUS "CMAKE_INSTALL_LIBDIR ${CMAKE_INSTALL_LIBDIR}")
message(STATUS "CMAKE_INSTALL_LIBEXECDIR ${CMAKE_INSTALL_LIBEXECDIR}")
message(STATUS "CMAKE_INSTALL_OLDINCLUDEDIR ${CMAKE_INSTALL_OLDINCLUDEDIR}")
message(STATUS "CMAKE_INSTALL_DIR ${CMAKE_INSTALL_DIR}")
message(STATUS "CONAN_CXX_FLAGS ${CONAN_CXX_FLAGS}")
message(STATUS "CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS}")
message(STATUS "CATCH_BUILD_STATIC_LIBRARY ${CATCH_BUILD_STATIC_LIBRARY}")
message(STATUS "CMAKE_INSTALL_SBINDIR ${CMAKE_INSTALL_SBINDIR}")

add_library(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/src/greeting.cpp
        include/greeting/greeting.h
        )

## https://cmake.org/cmake/help/latest/command/target_include_directories.html
target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>  # <prefix>/include/mylib
        ${CMAKE_CURRENT_SOURCE_DIR}/include)

target_compile_options(${PROJECT_NAME} PUBLIC "-Wextra" "-Werror"
                                    "$<$<CONFIG:RELEASE>:-O3>"
                                    "$<$<CONFIG:DEBUG>:-fsanitize=address>"
                                    "$<$<CONFIG:DEBUG>:-fno-omit-frame-pointer>")
target_link_options(${PROJECT_NAME} PUBLIC "$<$<CONFIG:DEBUG>:-fsanitize=address>")

target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
set_target_properties(${PROJECT_NAME} PROPERTIES INTERFACE_LINK_LIBRARIES CONAN_PKG::catch2)

# RPATH magic for *.dylibs to work properly, out of scope for now (might be obsolete already)

#target_link_libraries(${PROJECT_NAME} INTERFACE ${CONAN_TARGETS})
#set_target_properties(${PROJECT_NAME} PROPERTIES INSTALL_RPATH "$ORIGIN/:$$ORIGIN/../lib/")
#set_property(TARGET testlib::testlib PROPERTY INTERFACE_LINK_LIBRARIES

install(TARGETS greeting
        PUBLIC_HEADER DESTINATION include
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

enable_testing()
include(${CONAN_LIB_DIRS_CATCH2}/cmake/Catch2/Catch.cmake)

add_executable(${PROJECT_NAME}-test ${CMAKE_CURRENT_SOURCE_DIR}/tests/test.cpp)
target_link_libraries(${PROJECT_NAME}-test PUBLIC ${PROJECT_NAME} )

catch_discover_tests(${PROJECT_NAME}-test)
