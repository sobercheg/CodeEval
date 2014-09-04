__author__ = 'apuhach'
import math

P = 1000
N = int(P * math.log(P) + P * math.log(math.log(P)))
primes = 0

prime_marker = [True] * (N + 1)
sum = 0
for i in range(2, N + 1):
    if not prime_marker[i]:
        continue
    sum += i
    primes += 1
    if primes == P:
        break
    for j in range(i + i, N + 1, i):
        prime_marker[j] = False

print(sum)