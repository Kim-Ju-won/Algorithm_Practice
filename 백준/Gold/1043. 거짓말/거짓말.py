# 거짓말

# 지민이는 파티에 가서 이야기하는 것을 좋아함 
# 지민이 - 가장 좋아한는 이야기 
# 과장에서 말하는 경우가 있고, 그렇지 않은 경우가 있음 
# 진실을 아는 사람에게는 진실, 거짓을 하는 사람에게는 과장 
# 1<=n<=50 : 사람수, 1<=m<=50 파티수 
# 과장된 이야기를 할 수 있는 최댓 값 

import sys
from collections import deque


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

truth = sys.stdin.readline().split()
uf = [ i for i in range(n+1)]
count = 0 

if len(truth) == 1 : 
    count = 0 
else : 
    truth = list(map(int, truth))
    count = truth[0]
    truth = deque(truth[1:])

    truth_checker = truth[0]

    if count >= 2 : 
        for t in truth : 
            union(uf, truth_checker, t)
    

    
    
parties = [ list(map(int, sys.stdin.readline().split())) for _ in range(m)]
party_checker = [True for _ in range(m)]
answer_set = set()
answer = 0 

if count == 0 : 
    print(m)
else : 
    while truth : 
        t = truth.popleft()
        for idx, party in enumerate(parties) : 
            can = True
            p_count, member = party[0], party[1:]
            if party_checker[idx] : 
                for i in range(p_count): 
                    if t == find(uf, member[i]) : 
                        can = False 

            if can is False  :
                for i in range(p_count):
                    union(uf, truth_checker, member[i])
                    truth.append(member[i]) 
                party_checker[idx] = False 
                m -= 1
        
    print(m)
