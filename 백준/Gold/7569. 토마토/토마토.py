import sys
from collections import deque

m, n, h = tuple(map(int ,sys.stdin.readline().split()))

tomato = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
    tomato.append(temp)

#[h][n][m]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1: 
                q.append((i,j,k))

while q : 
    x,y,z = q.popleft()
    if x+1 < h and tomato[x+1][y][z] == 0:
        tomato[x+1][y][z] = tomato[x][y][z] + 1 
        q.append((x+1,y,z))
    if y+1 < n and tomato[x][y+1][z] == 0:
        tomato[x][y+1][z] = tomato[x][y][z] + 1 
        q.append((x,y+1,z))
    if z+1 < m and tomato[x][y][z+1] == 0:
        tomato[x][y][z+1] = tomato[x][y][z] + 1 
        q.append((x,y,z+1))
    if x-1 >= 0 and tomato[x-1][y][z] == 0:
        tomato[x-1][y][z] = tomato[x][y][z] + 1 
        q.append((x-1,y,z))
    if y-1 >= 0  and tomato[x][y-1][z] == 0:
        tomato[x][y-1][z] = tomato[x][y][z] + 1 
        q.append((x,y-1,z))
    if z-1 >= 0 and tomato[x][y][z-1] == 0:
        tomato[x][y][z-1] = tomato[x][y][z] + 1 
        q.append((x,y,z-1))

max_num = 0 
check = 0 

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] != 0:
                check+=1 
                max_num = max(max_num, tomato[i][j][k])

if check == n*m*h : 
    print(max_num-1)
else : 
    print(-1)
