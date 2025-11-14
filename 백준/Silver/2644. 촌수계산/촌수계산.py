import sys
from collections import deque

n = int(sys.stdin.readline())

p1, p2 = tuple(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [ -1 for _ in range(n+1)]

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)
    
q = deque([(p1, 0)])
visited[p1] = 0

while q : 
    v, chon = q.popleft()
    for u in graph[v]:
        if visited[u] == -1 : 
            q.append((u, chon+1))
            visited[u] = chon + 1

print(visited[p2])