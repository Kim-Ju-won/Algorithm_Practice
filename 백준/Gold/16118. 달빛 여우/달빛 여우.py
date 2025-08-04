import heapq
import sys

INT_MAX = sys.maxsize
n, m = tuple(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
pq = []
wolf_dist = [[INT_MAX] * (n + 1) for _ in range(2)]
fox_dist = [INT_MAX] * (n + 1)
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

for i in range(1, m + 1):
    x, y, z = edges[i - 1]
    graph[x].append((y, 2 * z))
    graph[y].append((x, 2 * z))

fox_dist[1] = 0
heapq.heappush(pq, (0, 1))

while pq:
    min_dist, min_index = heapq.heappop(pq)
    if min_dist == fox_dist[min_index]:
        for target_index, target_dist in graph[min_index]:
            new_dist = fox_dist[min_index] + target_dist
            if fox_dist[target_index] > new_dist:
                fox_dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))


wolf_dist[0][1] = 0
heapq.heappush(pq, (0, 1, 0))

while pq:
    min_dist, min_index, state = heapq.heappop(pq)
    if min_dist == wolf_dist[state][min_index]:
        for target_index, target_dist in graph[min_index]:
            if state == 0:
                new_dist = min_dist + (target_dist // 2)
                next_state = 1
            else:
                new_dist = min_dist + 2 * target_dist
                next_state = 0
            if wolf_dist[next_state][target_index] > new_dist:
                wolf_dist[next_state][target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index, next_state))

count = 0
for i in range(2, n + 1):
    if min(wolf_dist[0][i], wolf_dist[1][i]) > fox_dist[i]:
        count += 1
print(count)
