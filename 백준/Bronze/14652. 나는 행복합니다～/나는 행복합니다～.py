import sys
n, m, k = tuple(map(int, sys.stdin.readline().split()))
print(k // m, (k % m) % n)