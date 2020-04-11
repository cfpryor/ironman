#!/bin/bash

readonly BASE_DIR=$(realpath "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )")

readonly SCRIPTS_DIR="${BASE_DIR}/scripts"

function main() {
   trap exit SIGINT
}

function run() {
   pushd . > /dev/null

   cd "$(dirname ${SCRIPTS_DIR})"
   python3 generate.py

   popd > /dev/null
}

main "$@"
