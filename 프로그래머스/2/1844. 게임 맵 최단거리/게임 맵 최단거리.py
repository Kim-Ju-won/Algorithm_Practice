from collections import deque

def in_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False
    
    
def solution(maps):
    n, m= len(maps), len(maps[0])
    visited = [[ False for _ in range(m)] for _ in range(n)]
    
    x, y = [1,0,-1,0], [0,1, 0, -1]
    q = deque([(0,0,1)])
    visited[0][0] = True
    checker = False
    answer = 0 
    while q : 
        i, j, count = q.popleft()
        for dx, dy in zip(x, y):
            
            if in_range(i+dx, j+dy, n, m) and visited[i+dx][j+dy] == False and maps[i+dx][j+dy] == 1:
                q.append((i+dx, j+dy, count+1))
                visited[i+dx][j+dy] = True
                if i+dx == n-1 and j+dy == m-1 : 
                    answer = count+1
                    checker = True 
        if checker == True : 
            break
    
    
    return answer if checker else -1