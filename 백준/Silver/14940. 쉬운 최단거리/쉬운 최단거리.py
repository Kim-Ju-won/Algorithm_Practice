# 지도가 주어졌을 때 목표 지점까지의 거리 
# 움직이는 방향 - 수직, 수평

# 2 <= n, m <= 1000
# n = 세로의 길이, m = 가로의 길이
# 갈 수 없는 땅 0, 갈 수 있는 땅 1, 목표지점 2 

import sys
from collections import deque


def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False 

n, m = tuple(map(int, sys.stdin.readline().split()))
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
dx, dy = [1,0,-1,0], [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: 
            q = deque([(i,j,0)])
            visited[i][j] = 0
            
            while q : 
                r, c, count = q.popleft()
                for x, y in zip(dx,dy):
                    if in_range(r+x, c+y, n, m) and graph[r+x][c+y] == 1 and visited[r+x][c+y] == -1  : 
                        visited[r+x][c+y] = count + 1
                        q.append((r+x,c+y,count+1))
        elif graph[i][j] == 0 : 
            visited[i][j] = 0
                        
for i in range(n):
    for j in range(m):
        print(visited[i][j], end = " ")
    print()