import sys


def in_range(x, y, r, c):
    return True if 0 <= x < r and 0 <= y < c else False 

r, c, n = tuple(map(int, sys.stdin.readline().split()))
graph = [ list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
bomber = False
bombnum = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == "O":
            graph[i][j] = 0
            
for _ in range(n-1):
    if bomber : 
        for i in range(r):
            for j in range(c):
                if graph[i][j] == bombnum:
                    graph[i][j] = '.'
                    for x, y in zip(dx,dy):
                        if in_range(i+x,j+y,r,c) and graph[i+x][j+y] != bombnum :
                            graph[i+x][j+y] = '.'
        bombnum = 1-bombnum
    else : 
        for i in range(r):
            for j in range(c):
                if graph[i][j] != bombnum : 
                    graph[i][j] = 1-bombnum
    
    bomber = not(bomber)
    

for i in range(r):
    for j in range(c):
        if graph[i][j] == ".":
            print(graph[i][j], end= "")
        else : 
            print("O", end="")
    print()
    
 
