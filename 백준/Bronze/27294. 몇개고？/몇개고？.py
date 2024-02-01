import sys

t, a = tuple(map(int, sys.stdin.readline().split()))

if 12 <= t and t <= 16 and a != 1:
    print(320)
else:
    print(280)
