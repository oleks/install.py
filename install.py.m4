#!/usr/bin/env python3

# install.py — A simple, file-system-based install utility

# This file was generated from an m4 template.
m4_syscmd(`date -u --iso-8601=minutes |
  sed "s/^/# Generation date-time (ISO 8601): /"')m4_dnl
m4_syscmd(`git remote get-url origin |
  tr ":" "/" |
  sed "s/^git@/https:\\/\\//" |
  sed "s/\\.git$//" |
  sed "s/^/# Git repository URL: /"')m4_dnl
m4_format(`# Commit ID: %s', m4_include(HEAD_PATH))m4_dnl

m4_syscmd(`perl -pe "chomp if eof" LICENSE |
  sed "s/^/# /"')

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
