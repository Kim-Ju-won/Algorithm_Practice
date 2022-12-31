import sys 

a, b, c = list(map(int, sys.stdin.readline().split()))

if b >= c : 
    print(-1)
else : 
    x = 2100000001//2
    start = 0 
    end = 2100000001
    while True : 
        if a >= (c-b)*x and a < (c-b)*(x+1): 
            print(x+1)
            break
        elif a >= (c-b)*x: 
            start = x
            x = (x+end)//2
        elif a < (c-b)*x : 
            end= x
            x = (x+start)//2