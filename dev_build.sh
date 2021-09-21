#!/usr/bin/env bash

run() {
  echo -e "\e[36m ➤ $*\e[0m"
  "$@"
}

if ! command -v poetry > /dev/null 2>&1  ; then
  echo -e "\e[33mERROR: Python poetry is required. Install using:\e[0m\n"

  echo -e " \e[36m1. pipx[recommended]:\e[32m"
cat <<- EOF

    pip install -U pip wheel pipx # --user if needd
    pipx ensurepath
    source ~/.bashrc  # change to your shell's config name
    if command -v poetry &2>1 > /dev/null ; then pipx upgrade poetry ; else pipx install poetry ; fi
    pipx install poetry
EOF
echo -e "\n \e[36m2. pip:\e[32m\n"
cat <<- EOF
    pip install -U pip wheel poetry # --user if needed
    if command -v poetry &2>1 > /dev/null ; then pipx upgrade poetry ; else pipx install poetry ; fi
EOF


#   install poetry # preferred, or"
  echo "    pip install -U pip wheel poetry"
  exit 1
fi

current_dir=
echo $current_dir
if ! command -v conan > /dev/null &2>&1 ; then
  poetry shell

  poetry install ; fi
run poetry run conan source $(dirname $0)

#conan source .
#conan install . --install-folder=./build
#conan build . --build-folder=./build