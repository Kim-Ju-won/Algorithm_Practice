import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

a = A//C + 1 if A%C != 0 else A//C
b = B//D + 1 if B%D != 0 else B//D
print(L-max(a,b))
