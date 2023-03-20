import sys

a, b = tuple(map(int, sys.stdin.readline().split()))
a, b = max(a,b), min(a,b)
print((a+b)*(a-b+1)//2)

