#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

rm -rf $SCRIPT_DIR/../venv

python3 -m venv $SCRIPT_DIR/../venv

$SCRIPT_DIR/../venv/bin/python3 -m pip install pillow
