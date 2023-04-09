import sys

t = int(sys.stdin.readline())
fib = [[0,0] for _ in range(41)]

for i in range(41):
    if i == 0 : 
        fib[i][0] += 1
    elif i == 1 : 
        fib[i][1] += 1
    else : 
        for j in range(2):
            fib[i][j] = fib[i-1][j] + fib[i-2][j]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(*fib[n])