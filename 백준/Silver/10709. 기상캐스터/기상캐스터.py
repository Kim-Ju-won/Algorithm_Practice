import sys

h, w = tuple(map(int, sys.stdin.readline().split()))

graph = [ list(sys.stdin.readline()) for _ in range(h)]
visited = [[-1 for _ in range(w)] for _ in range(h)]

for count in range(w+1):
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'c' and visited[i][j] == -1: 
                visited[i][j] = count
    
    temp = [['.' for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'c' : 
                if j + 1 < w : 
                    temp[i][j+1] = graph[i][j] 

    for i in range(h):
        for j in range(w):
            graph[i][j]=temp[i][j] 
        


for i in range(h):
    for j in range(w):
        print(visited[i][j], end=" ")
    print()