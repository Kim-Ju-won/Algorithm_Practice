import sys
n = 100
while n > 0: 
    try: 
        s = sys.stdin.readline().rstrip()
        print(s)
        n-=1
    except : 
        break
