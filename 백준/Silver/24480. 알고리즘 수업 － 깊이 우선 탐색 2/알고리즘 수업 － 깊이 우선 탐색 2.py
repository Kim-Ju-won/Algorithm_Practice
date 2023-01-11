import sys
sys.setrecursionlimit(10**6)
n, m, s = tuple(map(int,sys.stdin.readline().split()))
visited = [0 for _ in range(n+1)]
edges = [ list() for _ in range(n+1)]
curr_time = 1
for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    edges[x].append(y)
    edges[y].append(x)

for i in range(len(edges)):
    edges[i].sort(reverse=True)

def dfs(edges, s):
    global curr_time
    visited[s] = curr_time
    curr_time+=1
    for i in edges[s]:
        if visited[i] == 0 : 
            dfs(edges,i)

dfs(edges, s)
for i in range(1, n+1):
    print(visited[i])