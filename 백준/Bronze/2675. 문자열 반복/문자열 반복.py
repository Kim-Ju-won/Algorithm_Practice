import sys 

t = int(sys.stdin.readline())
for i in range(t):
    n, s = sys.stdin.readline().rstrip().split()
    n = int(n)
    for i in range(len(s)) :
        print(s[i]*n, end ='')
    print() 
