import sys 

n, m = tuple(map(int ,sys.stdin.readline().split()))
a, b = max(n,m), min(n,m)

while b != 0 : 
    a, b = b, a%b

print((n//a)*m)