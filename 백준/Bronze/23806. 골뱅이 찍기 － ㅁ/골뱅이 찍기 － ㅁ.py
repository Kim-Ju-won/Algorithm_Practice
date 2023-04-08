import sys

n = int(sys.stdin.readline())

n = n*3*3

for i in range(0,n,n//3):
    if n % (i+n//3) == 0 : 
        for i in range(n//9):
            print('@'*(n//9)*5)
    else : 
        for i in range(n//3):
            print('@'*(n//9)+' '*(n//3)+'@'*(n//9))
