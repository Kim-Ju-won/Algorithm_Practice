import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
seq = []
def sequence(n, m, seq):
    if len(seq) == m : 
        for ele in seq : 
            print(ele, end=' ')
        print()
    else : 
        for i in range(1,n+1):
            seq.append(i)
            sequence(n, m, seq)
            seq.pop()
sequence(n, m, seq)