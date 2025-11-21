# 대면 수업 사람들 친해지기 
# 캠퍼스 N*M, 이동하는 방법 상,하,좌,우 
# 도연이는 캠퍼스 밖으로 이동불가 
# 만날 수 있는 사람의 수 
# I, O, P = 도연, 빈 공간, 사람 


import sys
from collections import deque


def in_range(x,y, n,m):
    return True if 0 <= x < n and 0 <= y < m else False

n, m = tuple(map(int, sys.stdin.readline().split()))

graph = [ sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[ False for _ in range(m)] for _ in range(n)]
dx, dy = [1,0,-1, 0], [0,1,0,-1]
q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            q.append((i,j))
            visited[i][j] = True
            break
    if q : 
        break
        
count = 0 
while q :
    r, c = q.popleft()
    for x, y in zip(dx, dy) : 
        if in_range(r+x, c+y, n, m) and graph[r+x][c+y] != 'X' and visited[r+x][c+y] is False : 
            if graph[r+x][c+y] == "P":
                count += 1
            visited[r+x][c+y] = True
            q.append((r+x, c+y))
            
if count : 
    print(count)
else : 
    print("TT")