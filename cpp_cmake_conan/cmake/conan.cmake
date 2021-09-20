macro(init_conan)
    # Download automatically, you can also just copy the conan.cmake file
    if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
        message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")

        # TODO: change to latest released version
        # currently develop branch contains Mac OS fix to use CMAKE_OSX_SYSROOT to specify SDK
        # fixes https://github.com/conan-io/cmake-conan/issues/296
        file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/develop/conan.cmake"
                "${CMAKE_BINARY_DIR}/conan.cmake"
                TLS_VERIFY ON)
    endif()

    include(${CMAKE_BINARY_DIR}/conan.cmake)

    conan_add_remote(NAME bincrafters
            INDEX 1
            URL https://api.bintray.com/conan/bincrafters/public-conan
            VERIFY_SSL True)
endmacro()
