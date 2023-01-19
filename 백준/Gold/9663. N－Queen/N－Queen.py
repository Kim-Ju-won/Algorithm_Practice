import sys 

n = int(sys.stdin.readline())
chess = [[ 0 for _ in range(n)] for _ in range(n)]
count = 0

def check_possibility(n,idx,chess):
    for i in range(n-1,-1,-1):
        if chess[i][idx] == 1 : 
            return False
    dy = 1
    for i in range(n-1,-1,-1):
        if idx-dy >= 0 : 
            if chess[i][idx-dy] == 1 : 
                return False
        if idx+dy < len(chess[n]) : 
            if chess[i][idx+dy] == 1 : 
                return False
        dy+=1
    return True

def n_queens(chess, n):
    global count 
    if n >= len(chess):
        return 
    for i in range(len(chess[n])):
        if check_possibility(n,i,chess):
            if n < len(chess) -1:
                chess[n][i] = 1
                n_queens(chess,n+1)
                chess[n][i] = 0
            elif n == len(chess)-1:
                count+=1

for i in range(len(chess[0])//2):
    if check_possibility(0,i,chess):
        chess[0][i] = 1
        n_queens(chess,1)
        chess[0][i] = 0

count *=2
if len(chess[0])%2 == 1 : 
    if check_possibility(0,len(chess[0])//2,chess):
        chess[0][len(chess[0])//2] = 1
        n_queens(chess,1)
        chess[0][len(chess[0])//2] = 0
if n == 1 : 
    print(count+1)
else : 
    print(count)