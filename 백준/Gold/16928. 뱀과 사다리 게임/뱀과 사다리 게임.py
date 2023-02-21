import sys 
from collections import deque
sys.setrecursionlimit(10**5)

n, m = tuple(map(int, sys.stdin.readline().split()))

graph = [ 0 for _ in range(101)]
visited = [0 for _ in range(101)]

for _ in range(m+n) : 
    s, e = tuple(map(int, sys.stdin.readline().split()))
    graph[s] = e 


def roll_the_dice(k):
    q = deque()
    q.append(k)
    while q : 
        start = q.popleft()
        if graph[start] != 0 : 
            visited[graph[start]] = visited[start]
            q.append(graph[start])
        else : 
            for i in range(1,7):
                if start + i <=100 and (visited[start+i] == 0 or visited[start]+1 < visited[start+i]): 
                    visited[start+i] = visited[start]+1
                    q.append(start+i)

roll_the_dice(1)
print(visited[100])
