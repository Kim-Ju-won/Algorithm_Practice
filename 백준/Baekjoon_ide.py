import sys 

t = int(sys.stdin.readline())

for _ in range(t):
    w, e = tuple(map(int, sys.stdin.readline().split()))
    ans = 1 
    for i in range(e,e-w,-1):
        ans *= i
    for i in range(1,w+1):
        ans //= i 
    print(ans)