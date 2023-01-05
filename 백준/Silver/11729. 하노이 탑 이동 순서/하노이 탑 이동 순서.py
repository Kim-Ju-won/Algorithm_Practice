import sys 

def hanoi(n):
    if n == 1 : 
        return 1
    else : 
        return hanoi(n-1)+1+hanoi(n-1)
def hanoi_route(n,a,b,c):
    if n == 1:
        print(a,c)
    else :
        hanoi_route(n-1,a,c,b)
        print(a,c)
        hanoi_route(n-1,b,a,c)
n = int(sys.stdin.readline())
print(hanoi(n))
hanoi_route(n,1,2,3)