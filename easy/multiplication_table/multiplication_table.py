__author__ = 'apuhach'
# https://www.codeeval.com/open_challenges/23/

N = 12

for i in range(1, N + 1):
    fmt = '%4d' * N
    print(fmt % tuple([i * j for j in range(1, N + 1)]))