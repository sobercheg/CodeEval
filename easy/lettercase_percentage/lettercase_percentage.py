__author__ = 'apuhach'

import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.rstrip()
        lower = len([c for c in line if c.lower() == c])
        upper = len(line) - lower
        print('lowercase: %.2f uppercase: %.2f' % (100 * lower / len(line), 100 * upper / len(line)))
