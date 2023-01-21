import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

DP = [1] * n 

for i in range(n):
    for j in range(0,i+1):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))