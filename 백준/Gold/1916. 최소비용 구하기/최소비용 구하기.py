# n개의 도시, 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스 
# A번째 도시에서 B번째 도시까지 가는데 드는 최소 버스 비용 
# 도시의 번호는 1~N

# 입력 1<=N<=1000 -> 도시의 갯수, 
# 둘째 줄 버스의 갯수 
# 셋째 줄에서 버스의 정보 
# 버스의 출발 -> 도착 도시 정보 
# 비용 -> 100000이하 자연수 
# M+3 우리가 구하고자 하는 출발점 도착 


import heapq
import sys

MAX_NUM = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cities = [MAX_NUM for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
pq = []
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y, cost = tuple(map(int, sys.stdin.readline().split()))
    graph[x].append((y,cost))
    
start, end = tuple(map(int, sys.stdin.readline().split()))

cities[start] = 0 

heapq.heappush(pq, (0, start))

while pq : 
    min_dist, min_index = heapq.heappop(pq)

    if min_dist == cities[min_index]:
        for target_index, target_dist in graph[min_index]:
            new_dist = cities[min_index] + target_dist 
            if cities[target_index] > new_dist : 
                cities[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))
                
print(cities[end])
