import sys
from collections import deque

n, m, v = tuple(map(int ,sys.stdin.readline().split()))
edges = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [ list() for _ in range(n+1)]
dfs_visited  = [ 0 for _ in range(n+1)]
bfs_visited = [ 0 for _ in range(n+1)]
dfs_count = 1

for edge in edges : 
    x, y = edge
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort()

def dfs(v, graph, dfs_visited):
    global dfs_count
    dfs_visited[v] = dfs_count
    dfs_count += 1
    for u in graph[v]:
        if dfs_visited[u] == 0 : 
            dfs(u, graph, dfs_visited)

def bfs(v, graph, count, bfs_visited):
    q = deque()
    bfs_visited[v] = count
    count+=1
    q.append(v)
    while q : 
        v = q.popleft()
        for u in graph[v]:
            if bfs_visited[u] == 0 : 
                bfs_visited[u] = count 
                count+=1
                q.append(u)


dfs(v, graph, dfs_visited)
bfs(v, graph, 1, bfs_visited)

dfs_order = dict()
bfs_order = dict()

for i in range(1,len(dfs_visited)):
    dfs_order[dfs_visited[i]] = i
for i in range(1, len(bfs_visited)):
    bfs_order[bfs_visited[i]] = i

dfs_keys = list(dfs_order.keys())
bfs_keys = list(bfs_order.keys())
dfs_keys.sort()
bfs_keys.sort()

for key in dfs_keys:
    if key != 0 : 
        print(dfs_order[key], end=' ')
print()
for key in bfs_keys : 
    if key != 0 : 
        print(bfs_order[key], end=' ')
