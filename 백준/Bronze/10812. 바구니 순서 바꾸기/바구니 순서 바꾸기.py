import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
basket = [ i for i in range(n+1)]

for _ in range(m):
    i, j, k = tuple(map(int, sys.stdin.readline().split()))
    temp = []
    for index in range(k,j+1):
        temp.append(basket[index])
    for index in range(i,k):
        temp.append(basket[index])
    basket[i:j+1] = temp

print(*basket[1:])