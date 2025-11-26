# N^N 그래프 / 홀수 인 자연수가 주어짐
# 달팽이 모양으로 중앙 부터 순회
# 1 <= N <= 999 -> 그리드 순회 시 100만
# 그래프를 순회하고, 주어진 값의 위치를 찾는 문제

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

move = [[-1,0], [0, 1], [1,0], [0, -1], [-1, 0]]
grid = [[ 1 for _ in range(n)] for _ in range(n)]


i, j = n//2, n//2
answer = f"{i+1} {j+1}"
direction = 0 
length = 2
direction_moved = 0 
count = 2

while count <= n*n : 
    x, y = move[direction]
    if direction == 0 : 
        i += x
        j += y
        grid[i][j] = count 
        count += 1
        direction += 1
    elif direction == 1 : 
        i += x
        j += y
        grid[i][j] = count  
        count += 1
        direction_moved += 1
        if direction_moved == length-1 : 
            direction += 1
            direction_moved = 0 
    elif direction == 2 : 
        i += x
        j += y
        grid[i][j] = count  
        count += 1
        direction_moved += 1
        if direction_moved == length : 
            direction += 1
            direction_moved = 0 
    elif direction == 3 : 
        i += x
        j += y
        grid[i][j] = count 
        count += 1
        direction_moved += 1
        if direction_moved == length : 
            direction += 1
            direction_moved = 0 
    elif direction == 4 : 
        i += x
        j += y
        grid[i][j] = count 
        count += 1
        direction_moved += 1
        if direction_moved == length : 
            direction = 0
            direction_moved = 0 
            length += 2
            
    if grid[i][j] == m : 
        answer = f'{i+1} {j+1}'

for i in range(n):
    for j in range(n):
        print(grid[i][j], end =" ")
    print()

print(answer)
