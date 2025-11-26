# N개의 막대 기둥 일렬로 세워져 있다. 
# 기둥들의 폭은 모두 1m 높이 다를 수 있음, 양철로 된 창고를 제작
# 창고에는 모든 기둥이 들어가도록 만들 것 

# 규칙
# 1. 지붕은 수평, 수직, 모두 연결되어 있기 
# 2. 수평 부분 어떤 기둥의 윗면과 닿아야 함 
# 3. 수직 부분은 반드시 어떤 옆면과 닿아야 함 
# 4. 지붕의 가장자리는 땅에 닿아야 함 
# 5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 함 

# 가장 면적이 작은 창고 -> 가장 높은 지붕을 기준으로 좌측, 우측 모두 내림차순으로 정렬이 되어야 함 
# 기둥의 개수 : N(1<= N <= 1000)
# 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H
# L, H 1000이하 

import sys

graph = [ 0 for _ in range(1000+1)]
l_graph = [ 0 for _ in range(1000+1)]
r_graph = [ 0 for _ in range(1000+1)]
l_max = [0,0]
r_max = [0,0]
min_i = 10001 
max_i = 0 

L = int(sys.stdin.readline())

for _ in range(L):
    l, h = tuple(map(int, sys.stdin.readline().split()))
    graph[l] = h
    min_i = min(l, min_i)
    max_i = max(l, max_i)

for i in range(min_i, max_i+1):
    if graph[i] >= l_max[0]:
        l_max[0] = graph[i]
        l_max[1] = i
    l_graph[i] = l_max[0]
    

for i in range(max_i, min_i-1, -1):
    if graph[i] >= r_max[0]:
        r_max[0] = graph[i]
        r_max[1] = i
    r_graph[i] = r_max[0]
    

print(sum(l_graph[min_i:r_max[1]])+sum(l_graph[r_max[1]:l_max[1]])+sum(r_graph[l_max[1]:max_i+1]))