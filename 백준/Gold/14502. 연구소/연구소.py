import sys
from collections import deque
from itertools import combinations


def in_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False

n, m =  tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
candidate_list = []
virus_list = deque([])
dx, dy = [1,0,-1,0], [0,1,0,-1]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 : 
            candidate_list.append((i,j))
        if arr[i][j] == 2 : 
            virus_list.append((i,j))

combination_list = list(combinations(candidate_list, 3))
answer = 0 

for idx, walls in enumerate(combination_list):
    graph = [[ 0 for _ in range(m)] for _ in range(n)]
    virus_list_temp = deque([])
    
    for virus in virus_list : 
        virus_list_temp.append(virus)
    #print(virus_list_temp)
    for i in range(n):
        for j in range(m):
            graph[i][j] = arr[i][j]
            
    for wall in walls :
        i, j = wall
        graph[i][j] = 1
        
    while virus_list_temp : 
        i, j = virus_list_temp.popleft()
        for x,y in zip(dx, dy):

            if in_range(x+i, y+j, n, m) and graph[x+i][y+j] == 0 : 
                graph[x+i][y+j] =2
                virus_list_temp.append((x+i,y+j))

    count = 0 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 : 
                count += 1

    answer = max(count, answer)

print(answer)