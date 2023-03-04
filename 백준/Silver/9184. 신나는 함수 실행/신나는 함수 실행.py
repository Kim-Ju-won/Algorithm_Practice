import sys 

w_array=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                w_array[i][j][k] = 1
            elif i < j and j < k :
                w_array[i][j][k] = w_array[i][j][k-1] + w_array[i][j-1][k-1] - w_array[i][j-1][k]
            else : 
                w_array[i][j][k] = w_array[i-1][j][k] + w_array[i-1][j-1][k] + w_array[i-1][j][k-1] - w_array[i-1][j-1][k-1]

while True : 
    a, b, c = tuple(map(int, sys.stdin.readline().split()))
    if (a,b,c) ==(-1,-1,-1):
        break
    if a <= 0 or b <= 0 or c <= 0 : 
        print(f'w({a}, {b}, {c}) = {w_array[0][0][0]}')
    elif a > 20 or b > 20 or c > 20 :
        print(f'w({a}, {b}, {c}) = {w_array[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {w_array[a][b][c]}')
