# n가지 종류의 동전 -> 가치의 합 k원 
# 동전의 개수 최소 
# 1<=동전의 가치<=10000, 가치가 같은 동전 여러번 
# 1<= n <= 100
# 1<= k <= 10000

import sys

n, k = tuple(map(int, sys.stdin.readline().split()))
coins = [ int(sys.stdin.readline()) for _ in range(n)]

DP = [ sys.maxsize for _ in range(k+1)]

for coin in coins : 
    if coin <= k : 
        DP[coin] = 1

for i in range(1, k+1):
    for coin in coins : 
        if i - coin >= 0 : 
            DP[i] = min(DP[i-coin]+1, DP[i])

if DP[-1] == sys.maxsize : 
    print(-1)
else : 
    print(DP[-1])
    