import sys 

a1, a0 = tuple(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())
if a1 - c > 0 : 
    print(0)
else : 
    if n0*a1 + a0 <= c*n0 : 
            print(1)
    else : 
        print(0)
