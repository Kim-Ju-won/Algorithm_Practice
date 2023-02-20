import sys

n = int(sys.stdin.readline())

for i in range(n-1): 
    print(' '*(n-1-i)+'*'*(i*2+1))
print('*'*(2*n-1))
for i in range(n-2,-1,-1): 
    print(' '*(n-1-i)+'*'*(i*2+1))