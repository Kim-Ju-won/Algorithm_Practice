import sys 
sys.setrecursionlimit(10**6)

def in_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False

def DFS(r1, c1, r2, c2, n, m, temp, blue_visited, red_visited, maze):
    global count
    dx, dy = [1,0,0,-1],[0,1,-1,0]
    
    if temp >= count : 
        return 
    if maze[r1][c1] == 3 and maze[r2][c2] == 4 : 
        count = min(count, temp)
    else : 
        if maze[r1][c1] == 3 : 
            for z, w in zip(dx, dy):
                if in_range(r2+z, c2+w, n, m) and blue_visited[r2+z][c2+w] != 1 and maze[r2+z][c2+w] != 5:
                    if (r1, c1) != (r2+z, c2+w):
                        blue_visited[r2+z][c2+w] = 1
                        DFS(r1,c1,r2+z,c2+w,n,m,temp+1,blue_visited,red_visited,maze)
                        blue_visited[r2+z][c2+w] = 0

        elif maze[r2][c2] == 4: 
            for x, y in zip(dx, dy):
                if in_range(r1+x, c1+y, n, m) and red_visited[r1+x][c1+y] != 1 and maze[r1+x][c1+y] != 5 :
                    if (r1+x, c1+y) != (r2, c2):
                        red_visited[r1+x][c1+y] = 1
                        DFS(r1+x,c1+y,r2,c2,n,m,temp+1,blue_visited,red_visited,maze)
                        red_visited[r1+x][c1+y] = 0
        else : 
            for x, y in zip(dx, dy):
                if in_range(r1+x, c1+y, n, m) and red_visited[r1+x][c1+y] != 1 and maze[r1+x][c1+y] != 5 :
                    for z, w in zip(dx, dy):
                        if in_range(r2+z, c2+w, n, m) and blue_visited[r2+z][c2+w] != 1 and maze[r2+z][c2+w] != 5:
                            if (r1+x, c1+y) != (r2+z, c2+w) and not((r1, c1) == (r2+z, c2+w) and (r1+x, c1+y) == (r2, c2)):
                                if maze[r1+x][c1+y] == 3 and maze[r2+z][c2+w] == 4 : 
                                    count = min(count, temp+1)
                                elif maze[r1][c1] == 3 and  maze[r2+z][c2+w] != 4 : 
                                    blue_visited[r2+z][c2+w] = 1
                                    DFS(r1,c1,r2+z,c2+w,n,m,temp+1,blue_visited,red_visited,maze)
                                    blue_visited[r2+z][c2+w] = 0
                                elif maze[r1+x][c1+y] != 3 and  maze[r2][c2] == 4 :
                                    red_visited[r1+x][c1+y] = 1
                                    DFS(r1+x,c1+y,r2,c2,n,m,temp+1,blue_visited,red_visited,maze)
                                    red_visited[r1+x][c1+y] = 0
                                else : 
                                    red_visited[r1+x][c1+y] = 1
                                    blue_visited[r2+z][c2+w] = 1
                                    DFS(r1+x,c1+y,r2+z,c2+w,n,m,temp+1,blue_visited,red_visited,maze)
                                    red_visited[r1+x][c1+y] = 0
                                    blue_visited[r2+z][c2+w] = 0


def solution(maze):
    global count
    n = len(maze)
    m = len(maze[0])
    blue_visited = [[ 0 for _ in range(m) ] for _ in range(n) ]
    red_visited = [[ 0 for _ in range(m) ] for _ in range(n) ]
    
    count = sys.maxsize
    # x, y -> 빨간색 시작 점 / z, w -> 파란색 시작 점
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1 : 
                r1, c1 = i, j 
                red_visited[i][j] = 1
            elif maze[i][j] == 2 : 
                r2, c2 = i, j 
                blue_visited[i][j] = 1

    DFS(r1,c1,r2,c2,n,m, 0,blue_visited,red_visited,maze)
    
    return 0 if sys.maxsize == count else count