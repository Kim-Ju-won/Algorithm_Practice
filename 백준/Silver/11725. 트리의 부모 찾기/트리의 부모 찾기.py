import sys
from collections import deque

n = int(sys.stdin.readline())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parents = [0] * (n + 1)
for i in range(n - 1):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    edges[x].append(y)
    edges[y].append(x)

q = deque()
q.append(1)
visited[1] = True
while q:
    k = q.popleft()
    for node in edges[k]:
        if visited[node] == False:
            visited[node] = True
            q.append(node)
            parents[node] = k

for ele in parents[2:]:
    print(ele)
