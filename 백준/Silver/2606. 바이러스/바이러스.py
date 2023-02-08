import sys
sys.setrecursionlimit(10**9)

computer = int(sys.stdin.readline())
n = int(sys.stdin.readline())
edges = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(computer+1)]
network = [ list() for _ in range(computer+1)]
for edge in edges : 
    x, y = edge
    network[x].append(y)
    network[y].append(x)

def dfs(s,network,visited):
    visited[s] = True 
    for net in network[s] : 
        if visited[net] == False:
            visited[net] == True
            dfs(net,network,visited)
dfs(1,network,visited)
print(visited[1:].count(True)-1)