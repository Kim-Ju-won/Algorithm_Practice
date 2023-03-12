import sys 

a1, b1 = tuple(map(int ,sys.stdin.readline().split()))
a2, b2 = tuple(map(int ,sys.stdin.readline().split()))
n, m = a1*b2 + a2*b1, b1*b2
p, q = max(n,m), min(n,m)

while q != 0 : 
    p,q = q, p%q

print(n//p, m//p)
