import sys

n = int(sys.stdin.readline())

wines = [0]+[ int(sys.stdin.readline()) for _ in range(n)]
DP = [ [0,0] for _ in range(n+1)]


for i in range(1, n+1):
    if i == 1 : 
        DP[i] = (wines[i], 1)
    elif i == 2 : 
        DP[i] = (wines[i]+DP[i-1][0], 2)
    elif i == 3 : 
        A = DP[i-2][0] + wines[i]
        B = DP[i-1][0]
        C = wines[i-1] + wines[i]
        
        DP_candidate = max(A, B, C)

        if DP_candidate == A : 
            DP[i] = (A, 1)
        elif DP_candidate == B : 
            DP[i] = (B, 0)
        elif DP_candidate == C : 
            DP[i] = (C, 2)
    else : 

        A = DP[i-3][0] + wines[i-1] + wines[i]
        if DP[i-3][1] == 1 : 
            B = DP[i-3][0] + wines[i-2] + wines[i]
        C = DP[i-1][0]
        D = DP[i-2][0] + wines[i]
        
        DP_candidate = max(A, B, C, D)
        
        if DP_candidate == A : 
            DP[i] = (A, 2)
        elif DP_candidate == B : 
            DP[i] = (B, 1)
        elif DP_candidate == C : 
            DP[i] = (C, 0)
        elif DP_candidate == D : 
            DP[i] = (D, 1)

print(DP[-1][0])
