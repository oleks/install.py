#!/usr/bin/env python3

import argparse


def _main():
    pass


def _parse_args():
    arg_parser = argparse.ArgumentParser(
        deescription="A simple, file-system-based install utility")
    return arg_parser.parse_args()


def main():
    args = _parse_args()
    _main(args)


if __name__ == "__main__":
    main()
