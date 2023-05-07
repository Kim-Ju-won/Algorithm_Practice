import sys

A, B = tuple(map(int, sys.stdin.readline().split()))
M = (B - A) / 400
print(1 / (1 + 10**M))

