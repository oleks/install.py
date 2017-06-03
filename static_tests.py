#!/usr/bin/env python3

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


run(["flake8", "."])
run([
    "mypy",
    "--strict",
    "--ignore-missing-imports",
    "."])

sys.exit(exitcode)
