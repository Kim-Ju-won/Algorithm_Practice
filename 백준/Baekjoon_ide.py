import sys
n, m= tuple(map(int, sys.stdin.readline().split()))


grid = []

def sequence(grid, n, m):
    if len(grid) == m :
        for i in range(len(grid)):
            print(grid[i], end = ' ')
        print()
    else : 
        for i in range(1,n+1):
            if i not in grid :
                temp = [] 
                temp += grid
                temp.append(i)
                sequence(temp, n, m)

sequence(grid, n, m)
