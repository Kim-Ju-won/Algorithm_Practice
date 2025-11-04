import sys
from collections import deque 

n, m = tuple(map(int, sys.stdin.readline().split()))

edges = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
visited = [ False for _ in range(n)]

for edge in edges : 
    x, y = edge 
    x, y = x-1, y-1
    graph[x].append(y)
    graph[y].append(x)
    
count = 0 
for i in range(n):
    if visited[i] is False : 
        count += 1
        q = deque([i])
        visited[i] = True 
        while q : 
            v = q.popleft()
            for u in graph[v]:
                if visited[u] is False : 
                    q.append(u)
                    visited[u] = True

print(count)