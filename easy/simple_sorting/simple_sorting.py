__author__ = 'apuhach'
# https://www.codeeval.com/open_challenges/91/

import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        nums = list(map(float, line.split()))
        nums.sort()
        print(' '.join(map(lambda x: '%.3f' % x, nums)))