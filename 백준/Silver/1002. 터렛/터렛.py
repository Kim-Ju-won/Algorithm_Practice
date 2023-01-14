import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, sys.stdin.readline().split()))
    d = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
    if (x1, y1, r1) != (x2, y2, r2):
        if d > r1+r2 : 
            print(0)
        elif d == r1+r2 : 
            print(1)
        else : 
            if min(r1,r2) +d == max(r1,r2) :
                print(1)
            elif min(r1,r2) + d < max(r1,r2) :
                print(0)
            else : 
                print(2)
    else : 
        print(-1)

    
