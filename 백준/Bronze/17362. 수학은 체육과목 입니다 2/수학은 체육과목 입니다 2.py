import sys


n = int(sys.stdin.readline())
if n <= 5 : 
    print(n)
else : 
    n -= 5
    n %= 8 
    if n <= 4 :
        print(5-n)
    else : 
        print(n-3)

