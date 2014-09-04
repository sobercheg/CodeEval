__author__ = 'apuhach'
# https://www.codeeval.com/open_challenges/16/

import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        num = int(line)
        ones = 0
        while num > 0:
            if num % 2 == 1:
                ones += 1
            num //= 2
        print(ones)
