#!/usr/bin/env bash

##!/usr/bin/env bash
#
#run() {
#  echo -e "\e[36m ➤ $*\e[0m"
#  "$@"
#}
#
#if ! command -v poetry > /dev/null 2>&1  ; then
#  echo -e "\e[33mERROR: Python poetry is required. Install using:\e[0m\n"
#
#  echo -e " \e[36m1. pipx[recommended]:\e[32m"
#  cat <<- EOF
#
#    pip install -U pip wheel pipx # --user if needd
#    pipx ensurepath
#    source ~/.bashrc  # change to your shell's config name
#    if command -v poetry &2>1 > /dev/null ; then pipx upgrade poetry ; else pipx install poetry ; fi
#    pipx install poetry
#EOF
#echo -e "\n \e[36m2. pip:\e[32m\n"
#cat <<- EOF
#    pip install -U pip wheel poetry # --user if needed
#    if command -v poetry &2>1 > /dev/null ; then pipx upgrade poetry ; else pipx install poetry ; fi
#EOF
#
#
##   install poetry # preferred, or"
#  echo "    pip install -U pip wheel poetry"
#  exit 1
#fi
#
#current_dir=
#echo $current_dir
#if ! command -v conan > /dev/null &2>&1 ; then
#  poetry shell
#
#  poetry install ; fi
#run poetry run conan source $(dirname $0)
#
##conan source .
##conan install . --install-folder=./build
##conan build . --build-folder=./build

set -v
script_dir="/Users/inksplatters/dev/interview-exercises/libgreeting"

pushd "$script_dir" || true

echo "we are in: $(pwd)"

rm -rf build
mkdir build && cd build || true

dev_profile=libgreeting-dev
release_profile=libgreeting-release

cxxflags="-Werror -Wextra"
ldflags=""

darwin_libcplusplus() {
  if [[ $(uname) == "Darwin" ]]; then
    conan profile update settings.compiler.libcxx="libc++" "$0"
  fi
}

create_dev_profile() {
  conan profile new --detect --force "$dev_profile"
  if [[ $(uname) == "Darwin" ]]; then
      conan profile update settings.compiler.libcxx="libc++" "$dev_profile"
  fi


  echo env.CXXFLAGS=\""$cxxflags -fsanitize=address -fno-omit-frame-pointer\"" \
       env.LDFLAGS=\""$ldflags -fsanitize=address\"" | xargs -n1 -I{} conan profile update "{}" "$dev_profile"
}

create_release_profile() {
  conan profile new --detect --force "$release_profile"
  darwin_libcplusplus "$release_profile"

  conan profile update env.CXXFLAGS="\"$cxxflags\"" "$release_profile"
  conan profile update env.LDFLAGS="\"$ldflags\"" "$release_profile"
}

create_dev_profile
#create_release_profile

conan source -sf src ..
conan install -if . -pr "$dev_profile" --build=missing ..
conan build -sf src -if . ..

popd || true
