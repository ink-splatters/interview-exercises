cmake_minimum_required(VERSION 3.21)

project(greeting)

message(${CMAKE_BINARY_DIR})
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

# https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_generator.html#targets-approach
conan_basic_setup(TARGETS)

#message("The v)
#message("CATCH_ENABLE_WERROR=${CATCH_ENABLE_WERROR}")
#message("CMAKE_EXPORT_NO_PACKAGE_REGISTRY=${CMAKE_EXPORT_NO_PACKAGE_REGISTRY}")
#message("CMAKE_INSTALL_BINDIR=${CMAKE_INSTALL_BINDIR}")
#message("CMAKE_INSTALL_DATAROOTDIR=${CMAKE_INSTALL_DATAROOTDIR}")
#message("CMAKE_INSTALL_INCLUDEDIR=${CMAKE_INSTALL_INCLUDEDIR}")
#message("CMAKE_INSTALL_LIBDIR=${CMAKE_INSTALL_LIBDIR}")
#message("CMAKE_INSTALL_LIBEXECDIR=${CMAKE_INSTALL_LIBEXECDIR}")
#message("CMAKE_INSTALL_OLDINCLUDEDIR=${CMAKE_INSTALL_OLDINCLUDEDIR}")
#message("CMAKE_INSTALL_SBINDIR=${CMAKE_INSTALL_SBINDIR}")

list(APPEND SRC src/greeting.cpp
        src/include/api/greeting.h)

add_library(${PROJECT_NAME} ${SRC})

#
## https://cmake.org/cmake/help/latest/command/target_include_directories.html
target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src/include>
        $<INSTALL_INTERFACE:include/greeting>  # <prefix>/include/mylib
        ${CMAKE_CURRENT_SOURCE_DIR}/include)

#list(APPEND COMPILE_OPTS "-Wextra" "-Werror" "$<$<CONFIG:RELEASE>:-O3>")
#
#target_compile_options(${PROJECT_NAME} PUBLIC ${COMPILE_OPTS})
#set_target_properties(${PROJECT_NAME} PROPERTIES INSTALL_RPATH "$ORIGIN/:$$ORIGIN/../lib/")
#et_property(TARGET testlib::testlib PROPERTY INTERFACE_LINK_LIBRARIES

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_20)

install(TARGETS ${PROJECT_NAME}
        PUBLIC_HEADER DESTINATION include
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

#add_sub




