import sys

n = int(sys.stdin.readline())

DP = [ 0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1 : 
        DP[i] = 1
    elif i == 2 : 
        DP[i] = 2
    else : 
        DP[i] = DP[i-1] + DP[i-2]
        
print(DP[-1]%10007)