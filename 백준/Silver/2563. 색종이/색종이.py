import sys

grid = [[0 for _ in range(100)] for _ in range(100)]
n = int(sys.stdin.readline())

for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    for i in range(a,a+10 ):
        for j in range(b,b+10):
            grid[i][j] = 1 
ans = 0
for i in range(100):
    ans += grid[i].count(1)
print(ans)
