import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

C = A+B
C.sort()

for ele in C : 
    print(ele, end= " ")