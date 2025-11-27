# 전쟁 
# 우리 팀 - 흰색(W), 상대 팀 - 파란 색(B)
# 같은 팀까지 모여 있을 때 N명 -> N^2의 파워
# 우리 팀과 상대팀의 파워 출력 하기 
# 대각선 인접하지 않는다

# 1<= N, M <= 100

import sys
from collections import deque


def in_range(x,y, n,m):
    return True if 0 <= x < m and 0 <= y < n else False 

def calculate_power(i,j,n,m,color):
    dx, dy = [0,1,-1,0], [1,0,0,-1]
    
    q = deque([(i,j)])
    visited[i][j] = True
    count = 1
    
    while q :
        r, c = q.popleft()
        for x, y in zip(dx,dy):
            if in_range(r+x, c+y, n, m) and visited[r+x][c+y] is False and graph[r+x][c+y] == color : 
                count += 1
                visited[r+x][c+y] = True
                q.append((r+x, c+y))
                
    return count ** 2
    
n, m = tuple(map(int, sys.stdin.readline().split()))

graph = [ list(sys.stdin.readline().strip()) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]


blue = 0 
white = 0 

for i in range(m):
    for j in range(n):
        if graph[i][j] == "B" and visited[i][j] is False:
            blue += calculate_power(i,j,n,m,"B")
        elif  graph[i][j] == "W" and visited[i][j] is False:
            white += calculate_power(i,j,n,m,"W")


print(white, blue)