import sys 

while True : 
    n, m = tuple(map(int, sys.stdin.readline().split()))
    if (n,m) == (0,0) : 
        break
    if n > m : 
        print('Yes')
    else : 
        print('No')