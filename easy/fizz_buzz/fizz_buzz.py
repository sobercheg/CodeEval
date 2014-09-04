__author__ = 'apuhach'
# https://www.codeeval.com/open_challenges/1/
import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        result = ''
        A, B, N = map(int, line.split())
        for i in range(1, int(N) + 1):
            if not i % A == 0 and not i % B == 0:
                result += str(i)
            else:
                if i % A == 0:
                    result += 'F'
                if i % B == 0:
                    result += 'B'
            result += ' '
        print(result)
