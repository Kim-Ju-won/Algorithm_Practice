import sys 

n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = list(map(int, sys.stdin.readline().split()))
    stair = n%h if n%h != 0 else h
    num = n//h if n%h == 0 else n//h+1
    if num < 10 : 
        num = '0'+str(num)
    print(f'{stair}{num}')
