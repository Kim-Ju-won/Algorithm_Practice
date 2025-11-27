# 지구 온난화로 인해 섬의 일부가 바다에 잠겼음 
# 지구 온난화 계혹 될 경우 남해의 지도는 어떻게 바뀔지 궁금해졌다. 
# 지도 R * C 그리드 -> 'X'는 땅, '.'
# 50년 - 인접한 세칸 또는 네칸에 바다가 있는 땅은 모두 잠겨버림 
# 50년 후 지도 그리기 
# 섬의 개수 오늘날보다 적어질 것 지도의 크기도 작아져야함 
# 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형 
# 적어도 섬은 하나 존재 -> 최소 1
# 지도를 넘어가는 칸은 모두 바다
# R, C (범위 1이상 10이하)

import sys


def in_range(x,y,n,m):
    return True if 0 <= x < n and 0 <= y < m else False

r, c = tuple(map(int, sys.stdin.readline().split()))

graph = [ list(sys.stdin.readline().rstrip()) for _ in range(r)]
new_graph = [[ "" for _ in range(c) ] for _ in range(r)]

min_i, max_i, min_j, max_j = r, 0, c, 0

dx, dy = [1,0,-1,0], [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == ".":
            new_graph[i][j] = graph[i][j]
        elif graph[i][j] == "X":
            count = 0 
            for x, y in zip(dx,dy):
                if in_range(i+x, j+y, r, c): 
                    if graph[i+x][j+y] == '.':
                        count += 1
                else : 
                    count += 1
            if count >=3 : 
                new_graph[i][j] = "."
            else : 
                new_graph[i][j] = "X"
                
                
for i in range(r):
    for j in range(c):
        if new_graph[i][j] == "X":
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)


for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1): 
        print(new_graph[i][j],end = "")
    print()

