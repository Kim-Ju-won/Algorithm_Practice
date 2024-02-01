import sys 

t = int(sys.stdin.readline())
ans = []
for _ in range(t):
    n = int(sys.stdin.readline())
    sum_t = [0]*(n+1)

    for i in range(n+1):
        if i == 1 : 
            sum_t[i] = 1
        elif i == 2 : 
            sum_t[i] = sum_t[i-1] + 1
        elif i == 3 :
            sum_t[i] = sum_t[i-2] + sum_t[i-1] + 1
        elif i >= 4: 
            sum_t[i] = sum_t[i-1]+sum_t[i-2]+sum_t[i-3]

    print(sum_t[n])