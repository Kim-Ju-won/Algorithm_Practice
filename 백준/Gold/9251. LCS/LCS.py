import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
n = len(s1)
m = len(s2)
LCS = [[ 0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i != 0 :
            if j == 0 : 
                if s1[i] == s2[j] : 
                    LCS[i][j] =  1
                else : 
                    LCS[i][j] = LCS[i-1][j]
            else : 
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
                if s1[i] == s2[j] : 
                    LCS[i][j] = max(LCS[i][j], LCS[i-1][j-1]+1)
        elif  i == 0 and j == 0 : 
            if s1[i] == s2[j] : 
                LCS[i][j] = 1
        elif i == 0 :
            if s1[i] == s2[j] : 
                LCS[i][j] =  1
            else : 
                LCS[i][j] = LCS[i][j-1]

print(LCS[-1][-1])

