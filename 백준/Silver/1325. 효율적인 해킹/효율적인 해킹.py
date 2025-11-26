# 컴퓨터 n개의 회사 
# 김지민 -> 한번의 해킹으로 여러개의 컴퓨터를 해킹할 수 있는 컴퓨터를 해킹 
# 컴퓨터는 신뢰하지 않는 관계, 신뢰하는 관계로 이루어져있음 : 신뢰하는 관계가 서로 해킹 가능함 ㅁ
# 한번에 가장 많이 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램 작성 
# 신뢰하는 관계가 들어옴 
# 1<=n<=10000, 1<=m<=100000

import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))

    graph[y].append(x)
    
max_hacking = 0 
hacking_list = []
log = []

for i in range(1, n+1):
    visited = [ False for _ in range(n+1)]
    
    count = 0
    q = deque([i])
    visited[i] = True
    
    while q : 
        curr_c = q.popleft()
        count += 1
        for next_c in graph[curr_c] : 
            if visited[next_c] is False : 
                visited[next_c] = True
                q.append(next_c)
    
    if max_hacking < count : 
        max_hacking = count 
        hacking_list = [i]
    elif max_hacking == count : 
        hacking_list.append(i)

        
hacking_list.sort()

for ele in hacking_list : 
    print(ele, end=" ")
