import sys 

def MenOfPassion(A, n, count):
    sum_A = 0 
    for i in range(n):
        sum_A+=A[i]
        count+=1
    return count

n = int(sys.stdin.readline())
A = [ 0 for _ in range(n)]
print(MenOfPassion(A,n,0))
print(1)