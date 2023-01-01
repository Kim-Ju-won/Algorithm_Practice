import sys

n = int(sys.stdin.readline())

if n > 1 : 
    i = 2
    limit = n
    while i <= n : 
        if n % i == 0 : 
            print(i)
            n = n//i
        else : 
            i+=1