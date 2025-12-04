# 동혁, 친구들과 함께 여행 
# 도시가 n개 임의의 도시 사이 길 있을 수도 있고 없을 수도 있음
# 길이 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별하는 프로그램 
# 조건 : 같은 도시를 여러번 방문하는 것도 가능
# 1 <= n <= 200, 도시들의 수 1 <= m <= 1000, A->B, B<-A 가능 

# i번째 줄 : j번째 수 i번 도시와 연결 정보 

import sys


def find(uf, x): 
    if uf[x] == x: 
        return x 
    root_node = find(uf, uf[x])
    uf[x] = root_node 
    return root_node

def union(uf, x, y):
    x = find(uf,x)
    y = find(uf,y)
    uf[x] = y

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
uf = [ i for i in range(n+1)]

for i in range(n): 
    graph = [0]+list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if i+1 != j+1 : 
            if graph[j+1] == 1: 
                union(uf, i+1, j+1)

                
cities = list(map(int, sys.stdin.readline().split()))
answer_set = set()
for city in cities : 
    answer_set.add(find(uf, city))

if len(answer_set) == 1 : 
    print("YES") 
else : 
    print("NO")