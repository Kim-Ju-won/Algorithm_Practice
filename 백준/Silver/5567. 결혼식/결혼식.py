# 상근이 결혼식 
# 학교 동기, 자신의 친구, 친구의 친구 
# 동기 N명 
# 학번 1~N

# 친구 관계 리스트, 이 리스트 바탕으로 결혼식 초대할 수 
# 2 <= N <= 500, 1 <= m <= 10000

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)
    
answer = 0 
q = deque([(1,0)])
visited[1] = True

while q : 
    curr, count = q.popleft()
    for next_node in graph[curr]:
        if visited[next_node] is False : 
            visited[next_node] = True 
            q.append((next_node, count+1))
            if count + 1 <= 2 : 
                answer += 1

print(answer)
