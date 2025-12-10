# 미세먼지 제거 -> 공기청정기 설치 
# 집을 R X C인 격자판으로 나타냈고, 1X1 크기의 칸으로 나눴다 
# (r, c) -> r행, c열 의미 
# 공기 청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지 
# 공지 청정기가 설치되어 있지 않은 칸에는 미세먼지 양이 적혀있음 

# 미세먼지 확산 미세먼지가 있는 모든 칸에서 동시에 일어남, 인접한 네 방향으로 확산 
# 인접한 방향에 공기 청정기가 있거나 칸이 없으면 그 방향으로 확산이 일어나지 않음 
# 확산되는 양은 칸의 1//5 -> 소수점은 버림 
# 남은 미세먼지의 양은 A r/c -> 확산된 방향의 갯수 

# 공기 청정기 작동 
# 위쪽 바람은 반시계방향으로 순환
# 아래쪽 고기 청정기의 바람은 시계방향으로 순환 
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸 씩 이동 
# 공기 청정기에서 부는 바람은 미세먼지가 없는 바람 
# 공기 청정기로 들어간 미세먼지는 모두 정화 

# t초가 지난 구사과의 방에 남아있는 미세먼지 양을 구하기 
# 첫 째 줄  R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 
# 둘 째줄 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양

import sys
from collections import deque


def in_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False 

n, m, t = tuple(map(int, sys.stdin.readline().split()))
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx, dy = [1,0,-1,0], [0,1,0,-1]

air_purifier = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == -1 : 
            air_purifier.append([i,j])

upper_air_purifier = deque([(air_purifier[0][0], air_purifier[0][1])])
lower_air_purifier = deque([(air_purifier[1][0], air_purifier[1][1])])

for i in range(m):
    u_r, u_c = upper_air_purifier[-1]
    l_r, l_c = lower_air_purifier[-1]
    u_c += 1
    l_c += 1
    if in_range(u_r, u_c, n, m) : 
        upper_air_purifier.append((u_r, u_c))
    if in_range(l_r, l_c, n, m) : 
        lower_air_purifier.append((l_r, l_c))

for i in range(n):
    u_r, u_c = upper_air_purifier[-1]
    l_r, l_c = lower_air_purifier[-1]
    u_r -= 1
    l_r += 1
    if in_range(u_r, u_c, n, m) : 
        upper_air_purifier.append((u_r, u_c))
    if in_range(l_r, l_c, n, m) : 
        lower_air_purifier.append((l_r, l_c))
        

for i in range(m):
    u_r, u_c = upper_air_purifier[-1]
    l_r, l_c = lower_air_purifier[-1]
    u_c -= 1
    l_c -= 1
    if in_range(u_r, u_c, n, m) : 
        upper_air_purifier.append((u_r, u_c))
    if in_range(l_r, l_c, n, m) : 
        lower_air_purifier.append((l_r, l_c))
        
for i in range(n):
    u_r, u_c = upper_air_purifier[-1]
    l_r, l_c = lower_air_purifier[-1]
    u_r += 1
    l_r -= 1
    if graph[u_r][u_c] != -1 : 
        upper_air_purifier.append((u_r, u_c))
    if graph[l_r][l_c] != -1  : 
        lower_air_purifier.append((l_r, l_c))

upper_air_purifier.popleft()
lower_air_purifier.popleft()

for _ in range(t):
    q = deque([])
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 : 
                q.append((i,j))


    while q : 
        i, j = q.popleft()
        if graph[i][j]//5 >= 1 : 
            plus = graph[i][j]//5
            count = 0 
            for x, y in zip(dx, dy):
                if in_range(x+i, y+j, n, m) and graph[i+x][j+y] != -1 : 
                    new_graph[x+i][y+j] += plus
                    count += 1
            new_graph[i][j] += graph[i][j] - plus*count
        else : 
            new_graph[i][j] += graph[i][j]

    for i in range(n):
        for j in range(m):
            if new_graph[i][j] >0 :
                graph[i][j] = new_graph[i][j]


    temp_deque = deque([])
    for point in upper_air_purifier:
        r, c = point 
        temp_deque.append(graph[r][c])
    
    temp_deque.appendleft(0)
    temp_deque.pop()
    
    for idx in range(len(upper_air_purifier)):
        r, c = upper_air_purifier[idx]
        graph[r][c] = temp_deque[idx] 
        
    temp_deque = deque([])
    for point in lower_air_purifier:
        r, c = point 
        temp_deque.append(graph[r][c])
    
    temp_deque.appendleft(0)
    temp_deque.pop()
    
    for idx in range(len(lower_air_purifier)):
        r, c = lower_air_purifier[idx]
        graph[r][c] = temp_deque[idx] 
        
answer = 0 


for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 : 
            answer += graph[i][j]
    
print(answer)
    