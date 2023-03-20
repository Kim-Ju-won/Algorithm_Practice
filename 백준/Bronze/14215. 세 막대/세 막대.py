import sys

lines = list(map(int, sys.stdin.readline().split()))
lines.sort()

if lines[-1] < sum(lines[:2]):
    print(sum(lines))
else : 
    k = lines[-1] - sum(lines[:2]) + 1
    print(sum(lines)-k)