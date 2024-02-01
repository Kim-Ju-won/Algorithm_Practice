import sys 
x, y = tuple(map(int, sys.stdin.readline().split()))

print(x + y if y < x else y - x)