#!/usr/bin/env python3
# coding: utf-8


import os
import pdb
import sys


from .src import *


def main():
    args = parseArg()
    log = loger()
    if args.debug:
        log.setLevel(logging.DEBUG)
    outfile = os.path.abspath(args.output)
    if hget(args.url, outfile, args.num, quite=args.quite):
        log.setLevel(logging.INFO)
        log.info("Donwload success")


if __name__ == "__main__":
    main()
