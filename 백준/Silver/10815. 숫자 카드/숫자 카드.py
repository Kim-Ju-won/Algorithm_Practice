import sys 

n = int(sys.stdin.readline())
sangkun = set(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

for c in cards : 
    if c in sangkun : 
        print(1, end = ' ')
    else : 
        print(0, end = ' ')