import sys
from collections import deque
n = int(sys.stdin.readline())

q = deque()
for _ in range(n):
    operation = sys.stdin.readline().split()
    if operation[0] =='push':
        q.append(int(operation[1]))
    elif operation[0] == 'pop':
        if len(q) != 0 : 
            print(q.popleft())
        else : 
            print(-1)
    elif operation[0] == 'size':
        print(len(q))
    elif operation[0] == 'empty':
        if len(q) != 0 : 
            print(0)
        else : 
            print(1)
    elif operation[0] == 'front':
        if len(q) != 0 : 
            print(q[0])
        else : 
            print(-1)
    elif operation[0] == 'back':
        if len(q) != 0 : 
            print(q[-1])
        else : 
            print(-1)