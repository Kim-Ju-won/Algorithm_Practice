import sys

n = int(sys.stdin.readline())
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = 1
    elif i == 1:
        dp[1] = 2
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[-1])
