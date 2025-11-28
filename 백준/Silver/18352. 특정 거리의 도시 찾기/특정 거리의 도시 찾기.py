# 특정 거리의 도시 찾기 
# 어떤 나라에는 1~N번까지 단방향 도로 M개 도로의 거리 1
# 특정한 도시 X에서 출발 모든 도시 중에서 최단 거리 K인 도시 번호들을 출력하는 프로그램 
# 2 <= N < 300,000, 1<=M<=1000,000, 1 <= K <= 300,000, 1 <= X <= N

import sys
from collections import deque

n, m, k, x = tuple(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
visited = [ False for _ in range(n+1)]
count = 0

for _ in range(m):
    r,c = tuple(map(int, sys.stdin.readline().split()))
    graph[r].append(c)
    
answer = []

q = deque([(x, 0)])
visited[x] = True

while q : 
    curr, count = q.popleft()
    for next_node in graph[curr]:
        if visited[next_node] is False : 
            if count + 1 == k : 
                answer.append(next_node)
            q.append((next_node, count +1))
            visited[next_node] = True

    
if answer : 
    answer.sort()
    for ele in answer : 
        print(ele)
else : 
    print(-1)