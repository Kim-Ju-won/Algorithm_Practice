import sys 

while True : 
    x, y = tuple(map(int, sys.stdin.readline().split()))
    if (x,y) == (0,0):
        break
    if x % y == 0 : 
        print('multiple')
    elif y % x == 0 : 
        print('factor')
    else : 
        print("neither")
