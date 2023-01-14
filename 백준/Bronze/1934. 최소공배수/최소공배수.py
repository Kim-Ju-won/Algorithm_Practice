import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = tuple(map(int, sys.stdin.readline().split()))
    prime = 1
    a = max(n,m)
    b = min(n,m)
    while True :
        if a % b == 0 : 
            prime = b
            break
        a, b = b, a%b 
    print(n//prime*m)