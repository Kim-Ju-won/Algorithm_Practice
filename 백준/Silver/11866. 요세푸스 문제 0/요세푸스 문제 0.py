import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))
ans = []
queue = deque(range(1,n+1))

while len(queue) != 0 : 
    queue.rotate(-(m-1))
    ans.append(queue.popleft())
    
print('<',end='')
for ele in ans[:-1] : 
    print(ele, end=', ')
print(f'{ans[-1]}>',end='')