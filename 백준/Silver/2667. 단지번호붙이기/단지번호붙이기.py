import sys
sys.setrecursionlimit(10**9)
 
n = int(sys.stdin.readline())
graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
count =0
 
def DFS(x,y,n):
    global count
    visited[x][y] = 1 
    count+=1
    if y-1 >= 0 and visited[x][y-1] == 0 and graph[x][y-1] == '1':
        DFS(x,y-1,n)
    if y+1 < n and visited[x][y+1] == 0 and graph[x][y+1] == '1': 
        DFS(x,y+1,n)
    if x-1 >= 0 and visited[x-1][y] == 0 and graph[x-1][y] == '1': 
        DFS(x-1,y,n)
    if x+1 < n and visited[x+1][y] == 0 and graph[x+1][y] == '1':  
        DFS(x+1,y,n)

def DFSALL(n):
    global count
    num_village = 0
    village_count = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == '1' : 
                DFS(i,j,n)
                num_village+=1
                village_count.append(count)
                count=0
                
    return num_village, village_count

village, house = DFSALL(n)
house.sort()
print(village)
for ele in house:
    print(ele)