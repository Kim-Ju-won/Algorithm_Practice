import sys
from collections import deque

n, m, r = tuple(map(int, sys.stdin.readline().split()))
edges = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [ 0 for _ in range(n+1)]
order = 1
graph = [ list() for _ in range(n+1)]
q = deque()

for edge in edges : 
    x, y = edge
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort()

def BFS(start):
    global order 
    visited[start] = order
    order+=1
    q.append(start)
    while q : 
        u = q.popleft()
        for ele in graph[u]:
            if visited[ele] == 0 : 
                visited[ele]=order 
                order+=1
                q.append(ele)
    

BFS(r)
for i in range(1,n+1):
    print(visited[i])