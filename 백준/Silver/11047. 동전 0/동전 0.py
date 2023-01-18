import sys 

n, k = tuple(map(int, sys.stdin.readline().split()))
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
count = 0
for i in range(n-1,-1,-1):
    count += k//coin[i]
    k-= (k//coin[i])*coin[i]
    if k == 0 : 
        break

print(count)