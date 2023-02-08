import sys 
from collections import deque

n, k = tuple(map(int, sys.stdin.readline().split()))
graph = [ 0 for _ in range(100001)]
visited = [ 0 for _ in range(100001)]
def DFS(n,k,visited):
    q = deque()
    q.append(n)
    visited[n]=1
    count = 0 
    while q : 
        next_q = q.popleft()
        if next_q == k : 
            break 
        if next_q-1 >= 0 and visited[next_q-1]==0 :
            visited[next_q-1] = visited[next_q]+1  
            q.append(next_q-1)
        if next_q+1 < len(graph) and visited[next_q+1] == 0 : 
            visited[next_q+1] = visited[next_q]+1  
            q.append(next_q+1)
        if 2*next_q < len(graph) and visited[2*next_q] == 0 : 
            visited[2*next_q] = visited[next_q]+1  
            q.append(2*next_q)
DFS(n,k,visited)
print(visited[k]-1)