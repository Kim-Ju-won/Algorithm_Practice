import sys
from collections import deque


def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False

m, n, k = tuple(map(int, sys.stdin.readline().split()))
graph = [[0 for _ in range(n+1)] for _ in range(m+1)]
visited = [[False for _ in range(n+1)] for _ in range(m+1)]
dx, dy= [1,0,-1,0], [0,1,0,-1]

for _ in range(k):
    r1, c1, r2, c2 = tuple(map(int, sys.stdin.readline().split()))
    for i in range(r1, r2):
        for j in range(c1, c2):
            graph[j][i] = 1
    

answer = []
for i in range(m):
    for j in range(n):
        if visited[i][j] is False and graph[i][j] == 0 : 
            q = deque([(i,j)])
            visited[i][j] = True 
            count= 1
            
            while q : 
                r, c = q.popleft()
                for x, y in zip(dx,dy):
                    if in_range(r+x, c+y, m, n) and graph[r+x][c+y] == 0 and visited[r+x][c+y] is False : 
                        visited[r+x][c+y] = True
                        count += 1
                        q.append((r+x, c+y))
            answer.append(count)
                        
print(len(answer))
answer.sort()
for ele in answer : 
    print(ele, end= " ")