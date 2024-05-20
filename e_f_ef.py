#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dpc import EFile, FFile, generate_ef_lines
import sys

if __name__ == '__main__':
    e = EFile(sys.argv[1])
    f = FFile(sys.argv[2])

    ef_lines = generate_ef_lines(e.lines, f.lines)

    with open(sys.argv[3], mode='w', encoding='cp932') as fp:
        for line in ef_lines:
            fp.write(f'{line}\n')
