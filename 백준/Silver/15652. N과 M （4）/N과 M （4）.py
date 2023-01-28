import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
seq = []
def sequence(s, n, m, seq):
    if len(seq) == m : 
        for ele in seq : 
            print(ele, end=' ')
        print()
    else : 
        for i in range(s,n+1):
            seq.append(i)
            sequence(i, n, m, seq)
            seq.pop()
sequence(1, n, m, seq)