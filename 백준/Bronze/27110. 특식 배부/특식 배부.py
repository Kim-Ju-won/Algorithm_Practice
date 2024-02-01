import sys

n = int(sys.stdin.readline())

a, b, c = tuple(map(int, sys.stdin.readline().split()))
print(min(a, n) + min(b, n) + min(c, n))
