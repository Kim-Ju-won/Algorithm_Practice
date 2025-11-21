# 음식물 피하기 
# 코레스코 콘도미니엄 8층 3끼 식사 
# 음식물이 통로 중간 중간에 떨어져있음 
# 이러한 음식물은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기 됨

# 큰 음식물 찾기 

import sys
from collections import deque


def in_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False

n,m,t = tuple(list(map(int, sys.stdin.readline().split())))
graph = [[ 0 for _ in range(m+1)] for _ in range(n+1)]
visited = [[ False for _ in range(m+1)] for _ in range(n+1)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
max_size = -1

for _ in range(t):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    graph[x][y] = 1
    
    
for i in range(1, n+1):
    for j in range(1, m+1): 
        if graph[i][j] == 1 and visited[i][j] is False : 
            q = deque([(i,j)])
            size = 0
            visited[i][j] = True 
            
            while q : 
                r, c = q.popleft()
                size+=1
                for x, y in zip(dx, dy):
                    if in_range(r+x, c+y, n+1, m+1) and graph[r+x][c+y] == 1 and visited[r+x][c+y] is False : 
                        visited[r+x][c+y] = True
                        q.append((r+x, c+y))
                        
            max_size = max(size, max_size)


print(max_size)