# N*N 크기의 도시 , 1*1 크기의 칸으로 나눠져있음 
# r행 c열 , 1~r,1~c
# 집의 치킨 거리 = |r2-r1| + |c2-c1|
# 도시의 치킨거리 , 치킨거리의 합

# 도시의 정보 0, 1, 2 
# 0 빈칸, 1 집, 2 치킨 집 
# 1 <= 집의 갯수 <= 2N을 넘지 않고, 적어도 1개 존재 
# M <= 치킨집 갯수는 <= 13보다 작거나 같음 

# 치킨 폐업 m개를 남여야함 
# 도시의 치킨 거리가 언제 가장 작을지 

import sys
from itertools import combinations

n, m = tuple(map(int, sys.stdin.readline().split()))
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chicken_list = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2 : 
            chicken_list.append((i,j))

total_distance = 0
answer = 50 * 50 * 13 + 1
possible_chicken = combinations(chicken_list, m)
possible_chicken = list(possible_chicken)

for chicken_shops in possible_chicken : 
    total_distance = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1 : 
                distance = 50 * 50 + 1
                for chicken_shop in chicken_shops : 
                    x,y = chicken_shop
                    distance = min(distance, abs(i-x) + abs(j-y))
                total_distance += distance
    answer = min(total_distance, answer)

print(answer)
                