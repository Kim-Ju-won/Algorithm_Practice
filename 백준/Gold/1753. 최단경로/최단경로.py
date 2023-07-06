import heapq
import sys

MAX_SIZE = sys.maxsize
v_num, e_num = tuple(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline())
graph = [[] for _ in range(v_num + 1)]
for _ in range(e_num):
    u, v, w = tuple(map(int, sys.stdin.readline().split()))
    graph[u].append((v, w))

dist = [MAX_SIZE] * (v_num + 1)
parent = [None] * (v_num + 1)
dist[start] = 0
q = []
heapq.heappush(q, (dist[start], start))
while q:
    d, node = heapq.heappop(q)
    for v, w in graph[node]:
        if d + w < dist[v]:
            heapq.heappush(q, (d + w, v))
            dist[v] = d + w
            parent[v] = node

for ele in dist[1:]:
    if ele != MAX_SIZE:
        print(ele)
    else:
        print("INF")
