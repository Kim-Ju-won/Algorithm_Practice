# 톱니 바퀴 회전 
# 4개의 톱니 바퀴(8개의 정수)
# 맞닿아 있는 부분은 1, 5
# 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째는 정수의 방향
# 방향이 1인 경우는 시계방향, -1인 경우는 반시계 방향

import sys
from collections import deque

def clockwise(wheel):
    wheel.appendleft(wheel.pop())
    return wheel 
    
def counter_clockwise(wheel):
    wheel.append(wheel.popleft())
    return wheel

wheels = [deque([0])]+[deque(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(4)]
k = int(sys.stdin.readline())

for _ in range(k):
    num, direction = tuple(map(int, sys.stdin.readline().split()))
    
    move_wheels = [(num, direction)]
    check_direction = direction
    for i in range(num, 4):
        if wheels[i][2] != wheels[i+1][6]:
            check_direction = -check_direction
            move_wheels.append((i+1, check_direction))
        else : 
            break
    
    check_direction = direction
    for i in range(num, 1, -1):
        if wheels[i][6] != wheels[i-1][2]:
            check_direction = -check_direction
            move_wheels.append((i-1, check_direction))
        else : 
            break

            
    for move_wheel in move_wheels : 
        idx, d = move_wheel 
        
        if d == 1 : 
            wheels[idx] = clockwise(wheels[idx])
        else : 
            wheels[idx] = counter_clockwise(wheels[idx])
   

print(wheels[1][0] + wheels[2][0]*2 + wheels[3][0]*4 + wheels[4][0]*8)


