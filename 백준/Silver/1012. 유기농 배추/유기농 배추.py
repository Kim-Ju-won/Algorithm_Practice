import sys
sys.setrecursionlimit(10**9)
t = int(sys.stdin.readline())

def DFS(m,n,i,j,cabbage,visited):
    visited[i][j] = 1
    if j+1 < n and cabbage[i][j+1] == 1 and visited[i][j+1] == 0: 
        DFS(m,n,i,j+1,cabbage,visited)
    if j-1 >= 0 and cabbage[i][j-1] == 1 and visited[i][j-1] == 0: 
        DFS(m,n,i,j-1,cabbage,visited)
    if i+1 < m and cabbage[i+1][j] == 1 and visited[i+1][j] == 0: 
        DFS(m,n,i+1,j,cabbage,visited)
    if i-1 >= 0 and cabbage[i-1][j] == 1 and visited[i-1][j] == 0: 
        DFS(m,n,i-1,j,cabbage,visited)

def DFSALL(m,n,cabbage, visited):
    count = 0 
    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1 and visited[i][j] == 0 : 
                DFS(m,n,i,j,cabbage,visited)
                count+=1
    return count

for _ in range(t):
    m, n, k = tuple(map(int ,sys.stdin.readline().split()))
    cabbage = [[ 0 for _ in range(n)] for _ in range(m)]
    visited = [[ 0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x,y = tuple(map(int, sys.stdin.readline().split()))
        cabbage[x][y] = 1
    num = DFSALL(m,n,cabbage, visited)
    print(num)