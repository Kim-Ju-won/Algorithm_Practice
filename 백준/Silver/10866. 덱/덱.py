import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == 'push_front':
        d.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        d.append(int(op[1]))
    elif op[0] == 'pop_front':
        if len(d) != 0 : 
            print(d.popleft())
        else : 
            print(-1)
    elif op[0] == 'pop_back':
        if len(d) != 0 : 
            print(d.pop())
        else : 
            print(-1)
    elif op[0] == 'size':
        print(len(d))
    elif op[0] == 'empty':
        if len(d) != 0 : 
            print(0)
        else : 
            print(1)
    elif op[0] == 'front':
        if len(d) != 0 : 
            print(d[0])
        else : 
            print(-1)
    elif op[0] == 'back':  
        if len(d) != 0 : 
            print(d[-1])
        else : 
            print(-1)