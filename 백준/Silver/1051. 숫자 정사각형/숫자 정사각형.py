import sys


def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False

n, m = tuple(map(int, sys.stdin.readline().split()))
graph = [ list(sys.stdin.readline().rstrip()) for _ in range(n)]

dx, dy = [0,1,1], [1,0,1]
answer = 1

for i in range(n):
    for j in range(m):
        c = 1
        while True : 
        
            if i + c >= n or j + c >= m :
                break
            else : 
                checking = 0 
                
                answer = max(answer, 1)
                for x, y in zip(dx, dy):
                    if in_range(i+c*x, j+c*y, n, m) and graph[i][j] == graph[i+c*x][j+c*y] : 
                        checking += 1
                if checking == 3 : 
                    answer = max((c+1)*(c+1), answer)
            c += 1

print(answer)