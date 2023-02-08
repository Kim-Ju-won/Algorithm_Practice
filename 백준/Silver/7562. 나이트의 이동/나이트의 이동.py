import sys
from collections import deque
sys.setrecursionlimit(10**9)
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    visited = [[0 for _ in range(n)] for _ in range(n)]
    start = tuple(map(int, sys.stdin.readline().split()))
    finish = tuple(map(int, sys.stdin.readline().split()))
    q = deque()
    
    count  = 1
    x, y = start
    visited[x][y] = count
    q.append(start)
    
    while q:
        x,y = q.popleft()
        if (x,y) == finish : 
            break
        #1 
        if x+2 < n and y+1 < n and visited[x+2][y+1] == 0 : 
            visited[x+2][y+1] = visited[x][y] + 1
            q.append((x+2,y+1))
        #2
        if x+1 < n and y+2 < n and visited[x+1][y+2] == 0 : 
            visited[x+1][y+2] = visited[x][y] + 1
            q.append((x+1,y+2))
        #3
        if x-1 >= 0  and y+2 < n and visited[x-1][y+2] == 0 : 
            visited[x-1][y+2] = visited[x][y] + 1
            q.append((x-1,y+2))
        #4
        if x-2 >=0 and y+1 < n and visited[x-2][y+1] == 0 : 
            visited[x-2][y+1] = visited[x][y] + 1
            q.append((x-2,y+1))
        #5
        if x-2 >= 0 and y-1 >=0 and visited[x-2][y-1] == 0 : 
            visited[x-2][y-1] = visited[x][y] + 1
            q.append((x-2,y-1))
        #6
        if x-1 >=0 and y-2 >=0 and visited[x-1][y-2] == 0 : 
            visited[x-1][y-2] = visited[x][y] + 1
            q.append((x-1,y-2))
        #7
        if x+1 < n and y-2 >=0 and visited[x+1][y-2] == 0 : 
            visited[x+1][y-2] = visited[x][y] + 1
            q.append((x+1,y-2))
        if x+2 < n and y-1 >=0 and visited[x+2][y-1] == 0 : 
            visited[x+2][y-1] = visited[x][y] + 1
            q.append((x+2,y-1))
    x,y = finish
    print(visited[x][y]-1)
