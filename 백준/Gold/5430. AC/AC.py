import sys 
from collections import deque

t = int(sys.stdin.readline())
ans = []
for _ in range(t):
    op = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    front= True 
    error = False 
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    for o in op : 
        if o =='R':
            front = not(front)
        else : 
            if n >= 1 : 
                if front == True : 
                    arr.popleft()
                else : 
                    arr.pop()
                n-=1
            else : 
                print('error')
                error=True
                break
            
    if error == False : 
        if len(arr) >= 1:
            if front == True : 
                print('[',end='')
                for i in range(len(arr)-1) : 
                    print(arr[i],end=',')
                print(f'{arr[-1]}]')
            else : 
                print('[',end='')
                for i in range(len(arr)-1,0,-1) : 
                    print(arr[i],end=',')
                print(f'{arr[0]}]')
        else : 
            print('[]')
