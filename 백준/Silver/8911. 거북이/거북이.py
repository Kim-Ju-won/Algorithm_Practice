# 2차원 평면위 움직일 수 있는 거북이 로봇 
# 명령 4개 움직임 
# B, F: (이동), L, R: (회전)
# 이동한 거리를 포함한 가장 작은 직사각형의 넓이, 선분의 길이는 0

import sys

t = int(sys.stdin.readline())

directions = {
    'N': [1,0], 
    'S': [-1,0],
    'E': [0,1],
    'W': [0,-1], 
}

current_direction = ['N', directions['N']]
for _ in range(t):
    x, y = 0,0
    r1, r2, c1, c2 = 0, 0, 0, 0
    
    instructions = sys.stdin.readline().rstrip()
    
    for instruction in instructions : 
        if instruction == 'F'  : 
            move = current_direction[1]
            i, j = move
            y += i 
            x += j 
            r1 = min(r1, y)
            r2 = max(r2, y)
            c1 = min(c1, x)
            c2 = max(c2, x)
            
        elif instruction == "B" : 
            move = current_direction[1]
            i, j = move
            y -= i 
            x -= j 
            r1 = min(r1, y)
            r2 = max(r2, y)
            c1 = min(c1, x)
            c2 = max(c2, x)
            
        elif instruction == 'L':
            d = current_direction[0]
            
            if d == "N":
                d = "W"
            elif d == "S":
                d = "E"
            elif d == "E":
                d = "N"
            elif d == "W":
                d = "S"
                
            current_direction = [d, directions[d]]
        elif instruction == 'R':
            d = current_direction[0]
            if d == "N":
                d = "E"
            elif d == "S":
                d = "W"
            elif d == "E":
                d = "S"
            elif d == "W":
                d = "N"
            current_direction = [d, directions[d]]
        
    w = 0
    if r1 <= 0 and r2 > 0 :
        w = abs(r2) + abs(r1)
    else : 
        w = r2 - r1

    h = 0
    if c1 <= 0 and c2 > 0 :
        h = abs(c2) + abs(c1)
    else : 
        h = c2 - c1
    print(w*h)
