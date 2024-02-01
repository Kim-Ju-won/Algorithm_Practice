import sys

n = int(sys.stdin.readline())
graph = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


for i in range(n):
    for j in range(i + 1):
        if (i, j) == (0, 0):
            dp[i][j] = graph[i][j]
        else:
            if j == 0:
                dp[i][j] = dp[i - 1][j] + graph[i][j]
            elif i == j:
                dp[i][j] = dp[i - 1][j - 1] + graph[i][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j - 1] + graph[i][j], dp[i - 1][j] + graph[i][j]
                )

print(max(dp[n - 1]))
