import sys 

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
members = [
    list(map(int, sys.stdin.readline().split())) for _ in range(n)
]
min_diff = sys.maxsize
seq = []

def sequence(s, n, m, seq):
    global min_diff
    if len(seq) == n//2 : 
        Team1 = 0
        Team2 = 0
        seq_set = set(seq)
        for i in range(n):
            for j in range(n):
                A = i in seq_set
                B = j in seq_set
                if A and B : 
                    Team1 +=members[i][j]
                elif (not A) and (not B) : 
                    Team2 += members[i][j]
        min_diff = min(abs(Team1-Team2), min_diff)
    else : 
        for i in range(s,n):
            seq.append(i)
            sequence(i+1,n,m,seq)
            seq.pop()


sequence(0, n, n//2, seq)
print(min_diff)