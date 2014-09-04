__author__ = 'apuhach'
import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        reversed_split = [''.join(reversed(token)) for token in ''.join(reversed(line.rstrip())).split()]
        print(' '.join(reversed_split))
