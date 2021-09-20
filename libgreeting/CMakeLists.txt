project(libgreeting)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

# https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_generator.html#targets-approach
conan_basic_setup(TARGETS)

file(SRC src/greeting.cpp
        src/include/api/greeting.h)

add_library(${PROJECT_NAME} SHARED ${SRC} )

#target_compile_definitions(${PROJECT_NAME} PRIVATE _BUILDING_DLL)
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_20)

#target_link_libraries(${PROJECT_NAME} PUBLIC
#        CONAN_PKG::boost
#        )

#set_target_properties(${PROJECT_NAME} PROPERTIES INSTALL_RPATH "$ORIGIN/:$$ORIGIN/../lib/")

