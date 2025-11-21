# 강호 스타트링크 지각 
# 총 F층으로 이루어진 고층 건물, 스타트링크 위치 G층
# 현재 위치 S층 -> 엘리베이트를 통해 G층 이동 
# 특이한 엘리베이터 버튼은 2개 : (위오)U 버튼 U층, (아래로)D버튼 D층 -> 버튼으로 층을 이동할 수 없으면 가지 않음  
# 엘리베이터를 이용해서 G층에 갈 수 없다면 use the stairs 출력
# G층에 도착하기 위해서 버튼을 몇 번 눌러야 하는지 
# 엘리베이터는 1층 이상, U, D는 0일 수 있음 

import sys
from collections import deque

f, s, g, u, d = tuple(map(int, sys.stdin.readline().split()))

stairs = [0 for _ in range(f+1)]
visited_stairs = [False for _ in range(f+1)]

q = deque([(s, 0)])
visited_stairs[s] = True 

while q : 
    stair, buttons = q.popleft()
    
    if stair + u <= f and visited_stairs[stair + u] is False : 
        visited_stairs[stair+u] = True
        q.append((stair+u, buttons+1))
        stairs[stair+u] = buttons+1
        if stair + u == g : 
            break 
        
    if stair - d >= 1 and visited_stairs[stair - d] is False : 
        visited_stairs[stair-d] = True
        q.append((stair-d, buttons+1))
        stairs[stair-d] = buttons+1
        if stair - d == g : 
            break 
            
            
if visited_stairs[g] is False: 
    print("use the stairs")
else : 
    print(stairs[g])