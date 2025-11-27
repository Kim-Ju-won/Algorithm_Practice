# 요세푸스 문제 

# 1번 사람 오른쪽 2번 ... i+1번째 사람 i번째 오른쪽, N번째 오늘쪽에는 1번 사람이 앉아 있음 
# K번 사람을 우선 제거, 직전 제거된 사람의 오른쪽 K번째 사람을 제거 -> 제거된 사람의 순서 
# 요세푸스 순열 

# M명의 사람이 될 때마다 원을 돌리는 방향을 바꿈 -> (N, K, M) 반전 요세푸스 순열 
# N의 길이 5000, K 5000

import sys
from collections import deque

n, k, m = tuple(map(int, sys.stdin.readline().split()))

people_deque = deque([ i for i in range(1, n+1)])

k -= 1
start = 0
count = 0 
d = True
while people_deque : 
    if count == m : 
        count = 0 
        d = not(d)
    if d : 
        for _ in range(k):
            people_deque.append(people_deque.popleft())
    else : 
        for _ in range(k+1):
            people_deque.appendleft(people_deque.pop())
    print(people_deque.popleft()) 
    count += 1
