from collections import deque

def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False

def solution(land):
    
    n = len(land)
    m = len(land[0])
    p_grid = [[ False for _ in range(m)] for _ in range(n)]
    d_grid = [[ 0 for _ in range(m)] for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    count = 0 
    for i in range(n): 
        for j in range(m): 
            if p_grid[i][j] is False and land[i][j] == 1 : 
                q = deque([(i,j)])
                p_grid[i][j] = True
                routes = [(i,j)]
                while q : 
                    r, c = q.popleft()
                    for x, y in zip(dx, dy):
                        if in_range(r+x, c+y, n, m) and p_grid[r+x][c+y] == False and land[r+x][c+y] == 1: 
                            q.append((r+x,c+y))
                            p_grid[r+x][c+y] = True
                            routes.append((r+x,c+y))
                count += 1
                for route in routes : 
                    r, c = route 
                    p_grid[r][c] = len(routes)
                    d_grid[r][c] = count
    
    max_p = 0 
    for j in range(m):
        temp = 0
        checking = set([])
        for i in range(n):
            if d_grid[i][j] not in checking : 
                temp += p_grid[i][j]
                checking.add(d_grid[i][j])
        max_p = max(max_p, temp)
    


    return max_p

