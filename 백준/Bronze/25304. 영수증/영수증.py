import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
check = 0 

for i in range(1,n+1):
    price, num = tuple(map(int, sys.stdin.readline().split()))
    check += price*num

if x == check : 
    print('Yes')
else: 
    print('No')
