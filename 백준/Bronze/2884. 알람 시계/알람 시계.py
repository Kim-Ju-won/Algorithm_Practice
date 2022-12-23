import sys 

h, m = tuple(map(int, sys.stdin.readline().split()))

if m <45 : 
    m= m+60-45
    if h == 0 : 
        h = 23
    else : 
        h-=1
else : 
    m-=45
print(h, m)
