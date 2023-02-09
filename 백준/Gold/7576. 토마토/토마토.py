import sys
from collections import deque

m, n = tuple(map(int, sys.stdin.readline().split()))
tomato = [
    list(map(int, sys.stdin.readline().split())) for _ in range(n)
]

q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1 : 
            q.append((i,j))


while q : 
    x,y = q.popleft()
    if x+1 < n and tomato[x+1][y] == 0: 
        q.append((x+1,y))
        tomato[x+1][y] = tomato[x][y] + 1
    if x-1 >= 0 and tomato[x-1][y] == 0: 
        q.append((x-1,y))
        tomato[x-1][y] = tomato[x][y] + 1
    if y-1 >= 0 and tomato[x][y-1] == 0: 
        q.append((x,y-1))
        tomato[x][y-1] = tomato[x][y] + 1
    if y+1 < m and tomato[x][y+1] == 0: 
        q.append((x,y+1))
        tomato[x][y+1] = tomato[x][y] + 1
    
max_num = 0
check = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0 :
            check = -1
            break
        else : 
            max_num = max(tomato[i][j], max_num)
            check+=1
    if check == -1 : 
        break 
            
if check == m*n : 
    print(max_num-1)
else : 
    print(-1)


