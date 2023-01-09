import sys

n, m= tuple(map(int, sys.stdin.readline().split()))
matrix = [[0 for _ in range(n+1)]]
for _ in range(n) : 
    matrix.append([0]+list(map(int, sys.stdin.readline().split())))

query = []
for _ in range(m):
    x1, y1, x2, y2 = tuple(map(int, sys.stdin.readline().split()))
    query.append((x1, y1, x2, y2))

sum_matrix = [ [0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_matrix[i][j] = matrix[i][j] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]

for q in query : 
    x1, y1, x2, y2 = q 
    print(sum_matrix[x2][y2]-sum_matrix[x1-1][y2]-sum_matrix[x2][y1-1]+sum_matrix[x1-1][y1-1])