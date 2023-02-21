import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
basket = [ 0 for _ in range(n+1) ]
for _ in range(m):
    i,j,k = tuple(map(int, sys.stdin.readline().split()))
    for index in range(i,j+1):
        basket[index] = k 

for ele in basket[1:] : 
    print(ele, end = ' ')