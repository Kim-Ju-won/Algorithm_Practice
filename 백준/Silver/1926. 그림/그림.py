# 도화지 그림이 그려져있을 때 
# 그림의 개수, 그림 중 넓이가 가장 넣은 것의 넓이를 출력 
# 그림 = 1로 연결된 걸 한 그림, 가로나 세로로 연결된 것은 그림, 대각선 떨어진 그림 
# 그림의 널비 1의 갯수
# 1<= n<= 500, 1<= m <=500
import sys
from collections import deque


def in_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False

n, m = tuple(map(int, sys.stdin.readline().split()))

graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx, dy = [1,0, -1, 0], [0, 1, 0, -1]

paint = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] is False : 
            q = deque([(i,j)])
            visited[i][j] = True
            size = 0
            while q : 
                r, c = q.popleft()
                size += 1
                for x, y in zip(dx, dy):
                    if in_range(r+x, c+y, n, m) and visited[r+x][c+y] is False and graph[r+x][c+y] == 1 : 
                        visited[r+x][c+y] = True
                        q.append((r+x, c+y))
            paint.append(size)

if paint : 
    print(len(paint))
    print(max(paint))
else : 
    print(0)
    print(0)