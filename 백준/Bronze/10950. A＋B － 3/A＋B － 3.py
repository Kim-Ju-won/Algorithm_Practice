import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = tuple(map(int,sys.stdin.readline().split()))
    print(a+b)