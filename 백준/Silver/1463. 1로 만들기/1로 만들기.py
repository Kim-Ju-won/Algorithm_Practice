import sys

INT_MAX = sys.maxsize

n = int(sys.stdin.readline())
graph = [INT_MAX]* (n) + [0]

for i in range(n, 0, -1):
    if i*3 <= n: 
        graph[i] = min(graph[i+1]+1, graph[i*3]+1,graph[i*2]+1)
    elif i*2 <= n : 
        graph[i] = min(graph[i+1]+1, graph[i*2]+1)
    elif i+1 <= n : 
        graph[i] = graph[i+1]+1
print(graph[1])