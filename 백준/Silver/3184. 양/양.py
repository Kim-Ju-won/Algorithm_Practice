# 미키의 뒷마당 - 특정 수의 양, 배고픈 마당에 들어와 양을 공격 
# 마당 - 행/열 
# '.' - 빈필드, '#' - 울타리, 'o'-양, 'v'- 늑대
# 수평, 수직으로만 이동 -> 두 칸은 같은 영역 
# 마당에서 탈출 할 수 잇는 칸은 어떤 영역에도 속하지 않음 
# 양이 많으면 늑대에게 싸움을 걸 수 있고 이김, 그렇지 않은 경우 다 먹힘 
# 3 <= n, m <= 250
# 살아 있는 양과 늑대의 수

import sys
from collections import deque


def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False

n, m = tuple(map(int, sys.stdin.readline().split()))
graph = [ sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
sheep_total = 0 
wolf_total = 0 

for i in range(n):
    for j in range(m):
        if graph[i][j] != "#" and visited[i][j] is False : 
            sheep = 0 
            wolf = 0 
            
            visited[i][j] = True 
            if graph[i][j] == 'v':
                wolf += 1
            elif graph[i][j] == 'o':
                sheep += 1
            q = deque([(i,j)])
            
            while q : 
                r, c = q.popleft()
                for x,y in zip(dx,dy):
                    if in_range(r+x, c+y, n, m) and visited[r+x][c+y] is False and graph[r+x][c+y] != "#":
                        visited[r+x][c+y] = True 
                        q.append((r+x,c+y))
                        if graph[r+x][c+y] == 'v':
                            wolf += 1
                        elif graph[r+x][c+y] == 'o':
                            sheep += 1
                        
            if wolf >= sheep : 
                wolf_total += wolf
            else : 
                sheep_total += sheep

print(sheep_total, wolf_total)