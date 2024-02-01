import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
print(min(n//2, m//2))