import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
print("Yes" if n * 100 >= m else "No")
