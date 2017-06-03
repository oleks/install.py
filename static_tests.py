#!/usr/bin/env python3

import os.path
import subprocess
import sys
from typing import List

exitcode = 0


def run(command: List[str]) -> None:
    global exitcode
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError:
        exitcode = 1


extra_files = [
        os.path.join('hooks', 'pre-commit'),
        os.path.join('hooks', 'pre-push')
    ]

run(["flake8", "."] + extra_files)

mypy_cmd = [
        "mypy",
        "--strict",
        "--ignore-missing-imports"
    ]

run(mypy_cmd + ['.'])

for extra_file in extra_files:
    run(mypy_cmd + [extra_file])

sys.exit(exitcode)
