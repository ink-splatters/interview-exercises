project(greeting)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

# https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_generator.html#targets-approach
conan_basic_setup(TARGETS)

list(APPEND SRC src/greeting.cpp
        src/include/api/greeting.h)

add_library(${PROJECT_NAME} ${SRC})

# https://cmake.org/cmake/help/latest/command/target_include_directories.html
target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include/greeting>  # <prefix>/include/mylib
        ${CMAKE_CURRENT_SOURCE_DIR}/include)

list(APPEND COMPILE_OPTS "-Wextra" "-Werror" "$<$<CONFIG:RELEASE>:-O3>")

target_compile_options(${PROJECT_NAME} PUBLIC ${COMPILE_OPTS})
set_target_properties(${PROJECT_NAME} PROPERTIES INSTALL_RPATH "$ORIGIN/:$$ORIGIN/../lib/")
#et_property(TARGET testlib::testlib PROPERTY INTERFACE_LINK_LIBRARIES

# target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_20) TODO: uncomment, specify private / public




