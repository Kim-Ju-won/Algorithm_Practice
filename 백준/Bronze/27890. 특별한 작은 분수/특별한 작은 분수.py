import sys

x, N = tuple(map(int, sys.stdin.readline().split()))

for i in range(1, N + 1):
    x = (x // 2) ^ 6 if x % 2 == 0 else (2 * x) ^ 6
print(x)
