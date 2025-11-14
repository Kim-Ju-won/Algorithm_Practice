import sys
from collections import deque

LAND = 1 
SEA = 0

def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
counts = []
while True : 
    w, h = tuple(map(int, sys.stdin.readline().split()))
    if (w,h) == (0,0):
        break
    graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [ [False for _ in range(w)] for _ in range(h) ]
    count = 0 
    
    for r in range(h):
        for c in range(w):
            if visited[r][c] is False and graph[r][c] == 1:  
                count += 1
                q = deque([(r,c)])
                visited[r][c] = True 

                while q : 
                    i, j = q.popleft()
                    for x, y in zip(dx,dy):
                        if in_range(i+x, j+y, h, w) and graph[i+x][j+y] == 1 and visited[i+x][j+y] is False : 
                            visited[i+x][j+y] = True
                            q.append((i+x, j+y))

        
    print(count)
