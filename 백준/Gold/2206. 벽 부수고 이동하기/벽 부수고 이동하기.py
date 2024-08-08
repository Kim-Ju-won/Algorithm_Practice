import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))
maze = [sys.stdin.readline().rstrip() for _ in range(n)]
visited_0 = [[sys.maxsize for _ in range(m)] for _ in range(n)]
visited_1 = [[sys.maxsize for _ in range(m)] for _ in range(n)]


def BFS(n, m, maze):
    q = deque()
    i, j, w = 0, 0, 0
    visited_0[i][j] = 1
    q.append((i, j, w))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        i, j, w = q.popleft()
        if (i, j) == (n - 1, m - 1):
            break
        for k in range(4):
            if w == 0:
                if (
                    (0 <= i + dx[k] < n)
                    and (0 <= j + dy[k] < m)
                    and visited_0[i + dx[k]][j + dy[k]] == sys.maxsize
                    and maze[i + dx[k]][j + dy[k]] == "0"
                ):
                    visited_0[i + dx[k]][j + dy[k]] = visited_0[i][j] + 1
                    q.append((i + dx[k], j + dy[k], 0))
                elif (
                    (0 <= i + dx[k] < n)
                    and (0 <= j + dy[k] < m)
                    and visited_0[i + dx[k]][j + dy[k]] == sys.maxsize
                    and maze[i + dx[k]][j + dy[k]] == "1"
                ):
                    visited_1[i + dx[k]][j + dy[k]] = visited_0[i][j] + 1
                    q.append((i + dx[k], j + dy[k], 1))
            else:
                if (
                    (0 <= i + dx[k] < n)
                    and (0 <= j + dy[k] < m)
                    and visited_1[i + dx[k]][j + dy[k]] == sys.maxsize
                    and maze[i + dx[k]][j + dy[k]] == "0"
                ):
                    visited_1[i + dx[k]][j + dy[k]] = visited_1[i][j] + 1
                    q.append((i + dx[k], j + dy[k], 1))


BFS(n, m, maze)
print(
    -1 
    if (visited_0[n - 1][m - 1] == sys.maxsize)
    and (visited_1[n - 1][m - 1] == sys.maxsize)
    else min(visited_0[n - 1][m - 1], visited_1[n - 1][m - 1])
)