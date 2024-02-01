import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0] = arr[0]
        temp = arr[0]
    else:
        temp = max(temp + arr[i], arr[i])
        dp[i] = max(dp[i - 1], temp)

print(dp[-1])