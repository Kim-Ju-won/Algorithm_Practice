import sys

t = int(sys.stdin.readline())

for i in range(1,t+1):
    a,b= tuple(map(int, sys.stdin.readline().split()))
    print('Case #'+str(i)+':', a+b)
