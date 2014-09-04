__author__ = 'apuhach'
# https://www.codeeval.com/open_challenges/156/
import sys

with open(sys.argv[1], 'r') as f:
    result = ''
    for line in f:
        is_upper = True
        for c in line:
            if c.isalpha():
                result += (c.upper() if is_upper else c)
                is_upper = not is_upper
            else:
                result += c

    print(result)
