import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
sum_graph = [ [0 for _ in range(m+1)]for _ in range(n+1)]
k = int(sys.stdin.readline())

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1 : 
            sum_graph[i][j] = graph[i-1][j-1]
        if i == 1 and j != 1 :
            sum_graph[i][j] = sum_graph[i][j-1] + graph[i-1][j-1]
        if i != 1 and j == 1 : 
            sum_graph[i][j] = sum_graph[i-1][j] + graph[i-1][j-1]
        if i != 1 and j != 1 : 
            sum_graph[i][j] = sum_graph[i][j-1] + sum_graph[i-1][j] + graph[i-1][j-1] - sum_graph[i-1][j-1]

for _ in range(k): 
    r1, c1, r2, c2 = list(map(int, sys.stdin.readline().split()))
    

    answers = sum_graph[r2][c2] + sum_graph[r1-1][c1-1] - sum_graph[r2][c1-1] - sum_graph[r1-1][c2]

    print(answers)