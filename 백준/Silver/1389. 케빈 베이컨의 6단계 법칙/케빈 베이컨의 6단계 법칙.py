# 케빈 베이컨의 6단계 최소 법칙 : 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다. 
# 케빈 베이컨 게임 : 사람이 최소 몇단계 만에 이어질 수 있는지 계산하는 게임
# 케빈 베이컨 : 케빈 베이컨 게임을 했을 때 단계의 합이 가장 적은 사람 

# BOJ 유저 중에 케빈 베이컨 수가 가장 작은 사람 구하기 
# 2 <= n <= 100, 1 <= M M= 5000
# 친구가 한명도 없는 사람은 없음 

import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
KevinBacon = [ 0 for _ in range(n+1)]

for _ in range(m):
    x,y = tuple(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(1, n+1):
    visited = [ False for _ in range(n+1)]
    q = deque([(i, 0)])
    visited[i] = True
    temp_kevin_bacon = 0
    while q : 
        curr_node, count = q.popleft()
        temp_kevin_bacon += count 
        for next_node in graph[curr_node]:

            if visited[next_node] is False : 
                visited[next_node] = True 
                q.append((next_node, count +1))
     
    KevinBacon[i] = temp_kevin_bacon

answer = 1
answer_checker = KevinBacon[1]
for i in range(1, n+1):
    if answer_checker > KevinBacon[i] : 
        answer = i 
        answer_checker = KevinBacon[i]
        
print(answer)