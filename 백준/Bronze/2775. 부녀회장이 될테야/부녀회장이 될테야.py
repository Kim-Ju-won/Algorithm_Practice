import sys 

t = int(sys.stdin.readline())

apt = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    apt[0][i] = i 

for i in range(1,15):
    for j in range(1,15):
        apt[i][j] += (apt[i-1][j]+apt[i][j-1])

for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(apt[k][n])