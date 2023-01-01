import sys

grid = []
max_index =[0,0]
max_num = -1
for _ in range(9):
    grid.append(list(map(int, sys.stdin.readline().split())))


for i in range(9):
    for j in range(9):
        if max_num < grid[i][j]: 
            max_num = grid[i][j]
            max_index = [i+1,j+1]

print(max_num)
print(max_index[0], max_index[1])
