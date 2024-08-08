import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))
maze = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


def BFS(n, m, maze):
    q = deque()
    i, j = 0, 0
    visited[i][j] = 1
    q.append((i, j))
    while q:
        i, j = q.popleft()
        if (i, j) == (n - 1, m - 1):
            break
        if i + 1 < n and visited[i + 1][j] == 0 and maze[i + 1][j] == "1":
            visited[i + 1][j] = visited[i][j] + 1
            q.append((i + 1, j))
        if i - 1 >= 0 and visited[i - 1][j] == 0 and maze[i - 1][j] == "1":
            visited[i - 1][j] = visited[i][j] + 1
            q.append((i - 1, j))
        if j + 1 < m and visited[i][j + 1] == 0 and maze[i][j + 1] == "1":
            visited[i][j + 1] = visited[i][j] + 1
            q.append((i, j + 1))
        if j - 1 >= 0 and visited[i][j - 1] == 0 and maze[i][j - 1] == "1":
            visited[i][j - 1] = visited[i][j] + 1
            q.append((i, j - 1))

    return visited[n - 1][m - 1]


print(BFS(n, m, maze))
