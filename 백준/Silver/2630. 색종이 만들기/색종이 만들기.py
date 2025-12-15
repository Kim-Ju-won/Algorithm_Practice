# 정사각형의 종이 
# 파란색 = 1, 하얀색 = 0  
# n <= 128, 2의 거듭제곱
# 출력 : 하얀색 색종이수, 파란색 색종이 수 
# 2^n, 2^n 구간끼리 칠해져있음. 

import sys

sys.setrecursionlimit(10**6)

def DivideAndFind(graph, r, n, c, m):
    global blue
    global white

    if r == n or c == m : 
        return 
    start = graph[r][c]
    check = True
    
    for i in range(r, n):
        for j in range(c, m):
            if graph[i][j] != start : 
                check = False
                break
        if check is False : 
            break
    if check is True : 
        if start == 1 : 
            blue += 1
        else : 
            white += 1
    else : 
        DivideAndFind(graph, r, (r+n)//2, c, (c+m)//2)
        DivideAndFind(graph, (r+n)//2, n, c, (c+m)//2)
        DivideAndFind(graph, r, (r+n)//2, (c+m)//2, m)
        DivideAndFind(graph, (r+n)//2, n,(c+m)//2, m)

n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
global blue
global white 
count = 0 
blue = 0 
white = 0 

DivideAndFind(graph, 0, n, 0, n)
print(white)
print(blue)