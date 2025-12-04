# 사이클 게임 
# 두 명의 플레이어가 차례대로 돌아가며 진행하는 게임 
# 선 플레이어 - 홀수, 후 플레이어 짝수 
# 0~n-1 => 평면 상의 점 n개 
# 어느 세점도 일직선 위에 놓이지 않는다. 
# 매 차례 마다 플레이ㅓ 두점을 선택해서 연결하는 선분 -> 처음으로 사이클을 완성하는 순간 게임 종류 
# 사이클 C는 플레이어가 그린 선분들의 부분 집합 

# C에 속한 임의의 선분의 한 끝점에서 출발해서 모든 선분을 한번씩 만 지나서 출발점으로 돌아올 수 있다. 

# 몇번째 차례에서 사이클이 완성되었는지 판단하는 프로그램 작성 

# 입력에의 첫 번째 줄 -> 점의 개수  3<=n<=500,000


import sys
sys.setrecursionlimit(10**9)

def find(uf, x):
    if uf[x] == x : 
        return x 
    root_node = find(uf, uf[x])
    uf[x] = root_node 
    return root_node
    
def union(uf, x, y):
    x = find(uf, x)
    y = find(uf, y)
    uf[x] = y 
    
n, m = tuple(map(int, sys.stdin.readline().split()))
uf = [ i for i in range(n)]
answer = 0 
instructions = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
for i in range(m):
    a, b = instructions[i]
    if find(uf, a) != find(uf, b):
        union(uf, a, b)
    else : 
        answer = i + 1
        break 
        
print(answer)
        
