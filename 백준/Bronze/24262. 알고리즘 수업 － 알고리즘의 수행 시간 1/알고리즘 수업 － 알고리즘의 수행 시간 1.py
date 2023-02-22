import sys 

def MenOfPassion(A, n):
    global current 
    current+=1
    i = n//2
    return A[i]

n = int(sys.stdin.readline())
A = [ 0 for _ in range(n)]
current = 0
MenOfPassion(A,n)
print(current)
print(0)