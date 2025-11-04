import sys
from collections import deque


def in_range(x,y,n):
    return True if 0 <= x < n and 0 <= y < n else False 

n = int(sys.stdin.readline())
max_height = 100 
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
max_survival_region = 0
dx, dy = [1,0,-1,0],[0,1,0,-1]

for h in range(max_height+1): 
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    region = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] is False: 
                region += 1
                visited[i][j] = True
                q = deque([(i,j)])
                while q : 
                    r, c = q.popleft()
                    for x, y in zip(dx, dy):
                        if in_range(r+x, c+y, n) and graph[r+x][c+y] > h and visited[r+x][c+y] is False: 
                            q.append((r+x, c+y))
                            visited[r+x][c+y] = True
    
    max_survival_region = max(region, max_survival_region)
    
print(max_survival_region)