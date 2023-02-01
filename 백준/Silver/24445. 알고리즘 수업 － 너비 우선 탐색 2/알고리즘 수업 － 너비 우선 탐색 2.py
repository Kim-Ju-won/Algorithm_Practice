import sys
from collections import deque

n,m,r = tuple(map(int, sys.stdin.readline().split()))
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = [list() for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
order = 1
for edge in edges : 
    x,y = edge
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort(reverse=True)

def bfs(graph,visited,r,order):
    q = deque()
    visited[r] = order
    order+=1
    q.append(r)
    while q : 
        u = q.popleft()
        for v in graph[u]:
            if visited[v] == 0:
                visited[v] = order
                order+=1
                q.append(v)
    return visited


visited = bfs(graph, visited,r,order)

for i in range(1,n+1):
    print(visited[i])