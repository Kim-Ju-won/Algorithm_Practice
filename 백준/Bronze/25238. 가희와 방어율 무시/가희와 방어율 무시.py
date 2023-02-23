import sys 

defence, percent = tuple(map(int, sys.stdin.readline().split()))
if defence *(100-percent)/100 >= 100:
    print(0)
else : 
    print(1)