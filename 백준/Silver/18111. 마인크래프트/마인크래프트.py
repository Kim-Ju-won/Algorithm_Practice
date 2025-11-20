# 마인크래프트
# 1*1*1 블록들로 이루어진 3차원 세계, 자유롭게 땅을 파거나 집을 지을 수 있는 게임 
# 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 '땅고르기 작업' 진행 

# 1. 좌표 (i,j)의 가장 위에 있는 블록 제거 - 인벤토리 : 2초 
# 2. 인벤토리 블록 하나를 꺼내어 좌표 (i,j)의 가장 위에 있는 블록 위에 놓는다 : 1초 작업

# 작업에 걸리는 최소 시간 - 그땅에 높이 
# 인벤토리에는 B개의 블록, 땅의 높이, 256블록 초과 불가, 음수 불가 
# N, M, B -> 입력 
# i, j -> 출력

import sys

n, m, b = tuple(map(int, sys.stdin.readline().split()))
minecraft = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_time = 2 * 256 * 500 * 500 + 1
max_height = 0 

for height in range(257) : 
    inventory = b 
    time = 0 

    for i in range(n):
        for j in range(m):
            if height > minecraft[i][j] : 
                inventory -= (height-minecraft[i][j])
                time += (height-minecraft[i][j])
            else : 
                inventory += (minecraft[i][j]-height)
                time += (minecraft[i][j]-height)*2

    if inventory >= 0 : 
        if min_time > time : 
            min_time = time 
            max_height = height
        elif min_time == time : 
            if max_height < height : 
                max_height = height
        
    
print(min_time, max_height)