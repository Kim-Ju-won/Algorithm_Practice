# 톱니바퀴 
# T개 일렬로 1...T
# 톱니 N극, S극
# 톱니바퀴 개수 (1 <= T <= 1000)
# 톱니 바퀴 가장 왼쪽 순서대로 8개의 정수, 12시방향부터 시계 방향 
# N극은 0, S극은 1, 시계 1, 반대 시계 -1

# 12시방향이 S극인 톱니바퀴

import sys
from collections import deque

n = int(sys.stdin.readline())
wheels = [deque([0])]+[ deque(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
k = int(sys.stdin.readline())
moves = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]

def clockwise(arr):
    arr.appendleft(arr.pop())
    return arr

def counter_clockwise(arr):
    arr.append(arr.popleft())
    return arr 


for move in moves : 
    idx, d = move
    new_direction = d
    move_wheels = [(idx, d)]
    
    for i in range(idx-1, 0, -1):
        if wheels[i][2] != wheels[i+1][6]:
            new_direction = -new_direction
            move_wheels.append((i, new_direction))
        else : 
            break
                
    new_direction = d
    for i in range(idx+1, n+1):
        if wheels[i-1][2] != wheels[i][6]:
            new_direction = -new_direction
            move_wheels.append((i, new_direction))
        else : 
            break
            
    for move_wheel in move_wheels: 
        idx, d = move_wheel
        if d == 1 : 
            wheels[idx] = clockwise(wheels[idx])
        elif d == -1 : 
            wheels[idx] = counter_clockwise(wheels[idx])


    
answer = 0 
for wheel in wheels : 
    answer += wheel[0]
    
print(answer)
    