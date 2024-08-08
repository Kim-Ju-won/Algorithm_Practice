import sys
from collections import deque

n, m, s = tuple(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
q = deque()
count = 0
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
for edge in edges:
    x, y = edge
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()


def DFS(s):
    global count
    count += 1
    visited[s] = count
    for u in graph[s]:
        if visited[u] == 0:
            DFS(u)


DFS(s)
DFS_visited = dict()

for i, v in enumerate(visited):
    if v > 0:
        DFS_visited[v] = i
        visited[i] = 0

q.append(s)
count = 1
visited[s] = count
while q:
    u = q.popleft()
    for w in graph[u]:
        if visited[w] == 0:
            q.append(w)
            count += 1
            visited[w] = count

BFS_visited = dict()

for i, v in enumerate(visited):
    if v > 0:
        BFS_visited[v] = i
        visited[i] = 0
dkeys = sorted(list(DFS_visited.keys()))
bkeys = sorted(list(BFS_visited.keys()))
for i in dkeys:
    print(DFS_visited[i], end=" ")
print()
for i in bkeys:
    print(BFS_visited[i], end=" ")
