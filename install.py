#!/usr/bin/env python3

# install.py — A simple, file-system-based install utility
# See also https://github.com/oleks/install.py

# Copyright (c) 2017 Oleks <oleks@oleks.info>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import configparser
import os.path
import sys

from typing import List, Tuple

__VERSION = 0.1


class InvalidSrc(Exception):
    def __init__(self, message: str) -> None:
        Exception.__init__(self, message)


class InvalidDst(Exception):
    def __init__(self, message: str) -> None:
        Exception.__init__(self, message)


def _src_is_newer(src_path: str, dst_path: str) -> bool:
    """
    pre:: os.path.exists(src_path)
    pre:: os.path.exists(dst_path)
    """
    src_mtime = os.path.getmtime(src_path)
    dst_mtime = os.path.getmtime(dst_path)
    return src_mtime > dst_mtime


def _symlink(src_path: str, dst_path: str) -> None:
    """
    pre:: os.path.exists(src_path)
    pre:: os.path.exists(os.path.dirname(dst_path))
    """
    print("Installing {} as {}".format(src_path, dst_path))
    if os.path.exists(dst_path) and not _src_is_newer(src_path, dst_path):
        return
    link_path = os.path.relpath(src_path, os.path.dirname(dst_path))
    os.symlink(link_path, dst_path)


def _install_fname(fname: str, src_dir: str, dst_dir: str) -> None:
    """
    pre:: os.path.exists(os.path.join(src_dir, path))
    pre:: os.path.exists(dst_dir)
    """
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(dst_dir, fname)
    _symlink(src_path, dst_path)


def _mkdirp(path: str) -> None:
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise ValueError(
                "{} exists, but it is not a directory.".format(
                    path))
        else:
            return
    _mkdirp(os.path.dirname(path))
    os.mkdir(path)


def _main(fnames: List[str], src_dir: str, dst_dir: str) -> None:
    _mkdirp(dst_dir)
    for fname in fnames:
        _install_fname(fname, src_dir, dst_dir)


def _init() -> Tuple[List[str], str, str]:
    config = configparser.ConfigParser()
    if len(sys.argv) < 2:
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    else:
        config_path = sys.argv[1]
    config.read(config_path)
    src_dir = eval(config['install.py']['src_dir'])
    dst_dir = eval(config['install.py']['dst_dir'])
    fnames = eval(config['install.py']['files'])
    assert type(src_dir) is str
    assert type(dst_dir) is str
    assert type(fnames) is list
    assert all((isinstance(fname, str) for fname in fnames))
    src_dir = os.path.relpath(src_dir)
    dst_dir = os.path.relpath(dst_dir)
    return (fnames, src_dir, dst_dir)


def main() -> None:
    paths, src_dir, dst_dir = _init()
    _main(paths, src_dir, dst_dir)


if __name__ == "__main__":
    main()
