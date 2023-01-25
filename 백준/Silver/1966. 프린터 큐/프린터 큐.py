import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = tuple(map(int, sys.stdin.readline().split()))
    arr = deque(map(int, sys.stdin.readline().split()))
    new_arr = deque()
    for idx, ele in enumerate(arr) : 
        new_arr.append((ele,idx))
    arr = list(arr)
    arr.sort(reverse=True)
    idx = 0
    count = 1
    while True : 
        if new_arr[0][0] >= arr[idx] : 
            if new_arr[0][1] == m : 
                print(count)
                break
            else : 
                new_arr.popleft()
                count +=1
                idx+=1
        else : 
            new_arr.append(new_arr.popleft())
