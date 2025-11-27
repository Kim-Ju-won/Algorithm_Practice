# 5*5의 숫자판 

# 각각의 칸에는 숫자가 적혀있다. 
# 임의의 위치에서 시작, 인접해 있는 네 방향으로 다섯 번 이동, 각 칸에 적혀있는 숫자 6자리의 수 
# 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123 같은 수 만들 수 있음 
# 숫자 판이 주어졌을 때, 만들 수 있는 서로 다른 여섯자리의 수들의 갯수 

import sys


def in_range(x,y,n):
    return True if 0 <= x < n and 0 <= y < n else False

def dfs(i,j,count, temp):
    if count == 0 : 
        temp_string = ""
        for c in temp : 
            temp_string += c 
        answer_set.add(temp_string)
    else : 
        dx, dy = [1,0,-1,0], [0,1,0,-1]
        for x, y in zip(dx,dy):
            if in_range(i+x, j+y, 5) :
                temp.append(str(graph[i+x][j+y]))
                dfs(i+x, j+y, count-1, temp)
                temp.pop()
                
            
answer_set = set()
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        dfs(i,j,6,[])
print(len(answer_set))