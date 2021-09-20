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

if [[ ! "$#" ]] || [[ "$1" != "dev" && "$1" != "pack" ]]; then
  echo "usage: $0 [dev|pack]"
  exit 0
fi

pushd "$script_dir" || true

rm -rf build
mkdir build && cd build || true

dev_profile=libgreeting-dev
release_profile=libgreeting-release

create_profile() {
  conan profile new --detect  "$1"
    if [[ $(uname) == "Darwin" ]]; then
      conan profile update settings.compiler.libcxx="libc++" "$1"
    fi
}

create_release_profile() {
  create_profile "$release_profile"
  conan profile update env.CXXFLAGS="\"-Werror -Wextra -O3\"" "$release_profile"
}

create_dev_profile() {
  create_profile "$dev_profile"
  conan profile update env.CXXFLAGS="\"-Werror -Wextra -fsanitize=address -fno-omit-frame-pointer\"" "$dev_profile"
  conan profile update env.LDFLAGS="\"-fsanitize=address -fno-omit-frame-pointer\"" "$dev_profile"
}

create_dev_profile
create_release_profile

build() {
  conan source -sf src ..
  conan install -if . -pr "$1" --build=missing ..
  conan build -sf src -if . ..
  conan package -sf src -bf . -pf package ..
}
if [[ "$1" == "dev" ]]; then
  echo " --dev flow"
  build "$dev_profile"
elif [[ "$1" == "" || "$1" == "pack"  ]]; then
  echo " --pack flow"
  build "$release_profile"
  conan export-pkg \
    --force \
    -sf . \
    -bf . \
    -pf package \
    -pr "$release_profile" \
    -pr:b "$release_profile" \
    .. \
    ink-splatters/greeting


#  -pf package ink-splatters/greeting -sf src -bf . -pr "$release_profile" ..

fi

popd || true
