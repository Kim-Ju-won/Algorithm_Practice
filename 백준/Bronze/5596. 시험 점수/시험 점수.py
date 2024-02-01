import sys

s = sum(list(map(int, sys.stdin.readline().split())))
t = sum(list(map(int, sys.stdin.readline().split())))
print(max(s, t))
