n, m = tuple(map(int, input().split()))
r, c, d = tuple(map(int, input().split()))
room_grid = [ list(map(int, input().split())) for _ in range(n)]

def in_range(i,j, n,m):
    return True if 0 <= i < n and 0 <= j < m else False

direction = {
    0:[-1,0],# 북
    1:[0,1],# 동
    2:[1,0],# 남
    3:[0,-1]# 서
}

change_direction = {
    0:3,
    1:0,
    2:1,
    3:2
}

moving = True
while moving :
    if room_grid[r][c] == 0: 
        room_grid[r][c] = 2
    else : 
        check_empty = False 
        for key in direction : 
            x, y = direction[key]
            if in_range(r+x, c+y, n, m) and room_grid[r+x][c+y] == 0 : 
                check_empty = True
                
        if check_empty : 
            d = change_direction[d]
            x, y = direction[d]
            if in_range(r+x, c+y, n, m) and room_grid[r+x][c+y] == 0 : 
                r, c = r+x, c+y
        else : 
            x, y = direction[d]
            if in_range(r-x, c-y, n, m) and room_grid[r-x][c-y] != 1 :
                r, c = r-x, c-y
            else : 
                break
        
count = 0 
for i in range(n):
    for j in range(m):
        if room_grid[i][j] == 2 : 
            count += 1
print(count)