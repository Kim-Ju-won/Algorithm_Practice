import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))
locate = list(map(int, sys.stdin.readline().split()))
count = 0
queue = deque()

for i in range(1,n+1):
    queue.append(i)

for ele in locate : 
    ele = ele
    right_rotate = 0 
    left_rotate = 0 

    i = 0
    while True : 
        if ele == queue[i] : 
            break
        else : 
            if i >= len(queue):
                i-=len(queue)
            right_rotate += 1
            i += 1
    i = 0
    while True : 
        if ele == queue[i] : 
            break
        else : 
            if i < 0:
                i+=len(queue)
            left_rotate += 1
            i -= 1
    if left_rotate < right_rotate : 
        queue.rotate(left_rotate)
        count += left_rotate
    else : 
        queue.rotate(-right_rotate)
        count += right_rotate
    queue.popleft()
    
print(count)