#!/usr/bin/env bash

set -v
script_dir="/Users/inksplatters/dev/interview-exercises/libgreeting"


pushd "$script_dir" || true

mkdir build && cd build


conan profile new --detect --force libgreeting
conan profile upgrade settings.compiler.libcxx="libc++" libgreeting 
conan profile update settings.compiler.cppstd=20  libgreeting

conan source -sf src ..
conan install -pr:b libgreeting -if .
conan build -sf src -if . ..

popd || true
