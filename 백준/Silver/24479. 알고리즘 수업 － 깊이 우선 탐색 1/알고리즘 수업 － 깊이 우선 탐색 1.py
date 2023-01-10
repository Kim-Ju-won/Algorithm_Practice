import sys
sys.setrecursionlimit(10**6)
n, m, s = tuple(map(int, sys.stdin.readline().split()))

edges = [ list() for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]
curr_time = 0 

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    edges[x].append(y)
    edges[y].append(x)

for i in range(len(edges)):
    edges[i].sort()

def dfs(x,edges):
    global curr_time
    curr_time += 1
    visited[x] = curr_time
    for i in edges[x]:
        if visited[i] == 0: 
            dfs(i,edges)

dfs(s,edges)
for i in range(1,n+1):
    print(visited[i])
