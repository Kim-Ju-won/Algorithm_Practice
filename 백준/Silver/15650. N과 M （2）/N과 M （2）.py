import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
seq=[]
def sequence(n,m,k,seq):
    if len(seq) == m : 
        for ele in seq : 
            print(ele, end=' ')
        print()
    else : 
        for i in range(k,n+1):
            temp = []
            temp+=seq 
            temp.append(i)
            k+=1
            sequence(n,m,k,temp)

sequence(n,m,1,seq)