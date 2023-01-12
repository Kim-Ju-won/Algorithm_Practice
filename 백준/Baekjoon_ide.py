import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
gcd = -1
for i in range(1, min(n,m)+1):
    if n % i == 0 and m %i  == 0 : 
        gcd = i 
lcm = n * ( m//gcd)
print(gcd)
print(lcm)