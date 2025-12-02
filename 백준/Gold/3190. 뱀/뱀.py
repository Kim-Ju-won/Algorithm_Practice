# 'Dummy'라는 도스게임 
# 뱀이 나와서 기어다님, 사과를 먹으면 뱀 길이가 늘어남
# 자기자신 or 벽 부딪히면 게임이 끝남 

# 게임 - NXN 정사각 보드위에서 진행, 몇몇 칸 (사과). 보드의 상하좌우 끝에 벽이 있음 
# 게임 뱀은 맨 좌측 시작, 뱀의 길이 1 

# 뱀 움직임 
# 처음에 오른쪽을 향함 
# 매초 이동 
# 규칙 
# 1. 몸길이를 늘려 머리를 다음칸에 위치 
# 2. 벽이나 자기자신의 몸과 부딪히면 게임 끝 
# 3. 이동한 칸에 사과, 사과가 없어지고 꼬리는 움직이지 않음
# 4. 이동한 칸에 사과 없다면, 몸길이를 줄여서, 꼬리가 위치한 칸을 비워줌

# 2 <= n <= 100, 다음 줄 사과의 개수 
# K개의 줄에 사과 위치 
# 뱀의 방향 변환 횟수 L 
# 방향 정보 
# 게임 시간 X초 뒤 왼쪽, 오른쪽 방향 회전 L, D 

# 게임이 몇 초 후에 끝나는지 출력 

import sys
from collections import deque


def in_range(x,y,n):
    return True if 0 <= x < n and 0 <= y < n else False

def transform(move_d, change):
    # 왼쪽 90도
    if change == 'L':
        if move_d == 'N':
            move_d = 'W'
        elif move_d == 'S':
            move_d = 'E'
        elif move_d == 'E':
            move_d = 'N'
        elif move_d == 'W':
            move_d = 'S'
    # 오른쪽 90도
    elif change == 'D':
        if move_d == 'N':
            move_d = 'E'
        elif move_d == 'S':
            move_d = 'W'
        elif move_d == 'E':
            move_d = 'S'
        elif move_d == 'W':
            move_d = 'N'
    
    return move_d

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[0 for _ in range(n)] for _ in range(n)]
time = 0

# 사과 위치시키기
for _ in range(k):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    x, y = x-1, y-1
    graph[x][y] = 2

# 뱀 위치 시키기
graph[0][0] = 1

# 방향
direction = {
    'N':[-1, 0],
    'S':[ 1, 0],
    'E':[ 0, 1],
    'W':[ 0,-1]
}

change_direction = dict()

l = int(sys.stdin.readline())

for _ in range(l):
    t, d = sys.stdin.readline().split()
    change_direction[int(t)] = d


tail = deque([(0,0)])
i, j = 0, 0
move_d = 'E'
while True : 
    
    x, y = direction[move_d]
    
    if in_range(i+x, j+y, n):
        i += x
        j += y
        if graph[i][j] == 1 : 
            time += 1
            break
        else :  
            if graph[i][j] == 0 :
                graph[i][j] = 1 
                tail.append((i,j))
                r, c = tail.popleft()
                graph[r][c] = 0  
            elif graph[i][j] == 2: 
                graph[i][j] = 1 
                tail.append((i,j))
    
    else : 
        time+=1
        break
    
    time += 1
    if time in change_direction : 
        move_d = transform(move_d, change_direction[time])

print(time)

