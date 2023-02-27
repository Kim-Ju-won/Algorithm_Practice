import sys

L, P = tuple(map(int, sys.stdin.readline().split()))
article = list(map(int, sys.stdin.readline().split()))
num = L*P
for ele in article : 
    print(ele-num, end=' ')