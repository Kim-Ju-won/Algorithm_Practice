# 2<=n<=100개의 도시. 한 도시에서 출발하여 다른 도시에 도착하는 m(1<=m<=100,000)개의 버스가 있다.
# 버스 -> 1번 사용할 때 비용 존재 
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값

# 첫 째 줄 n 
# 둘 째 줄 버스의 개수 m 
# 셋 째 줄부터 m+2줄까지의 버스 
# 시작 도시 a ,도착 도시 b, 한 번 타는데 필요한 비용 c 

import sys

MAX_NUM = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dist = [[MAX_NUM for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    dist[i][i] = 0 

for _ in range(m):
    a, b, c = tuple(map(int, sys.stdin.readline().split()))
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] != MAX_NUM  : 
            print(dist[i][j], end = " ")
        else : 
            print(0, end = " ")
    print()