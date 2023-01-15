import sys 

def gcd(n,m):
    n , m= max(n,m), min(n,m)
    while True : 
        if n%m ==0 : 
            break
        n, m = m, n%m
    return m
t = int(sys.stdin.readline())
circles = list(map(int, sys.stdin.readline().split()))

for i in range(1,t):
   g=gcd(circles[0], circles[i])
   print(f'{circles[0]//g}/{circles[i]//g}')