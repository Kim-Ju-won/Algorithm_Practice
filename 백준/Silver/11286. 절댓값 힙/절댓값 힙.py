import heapq
import sys

n = int(sys.stdin.readline())
pq = []

for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0 : 
        if len(pq) >=1:
            print(heapq.heappop(pq)[1])
        else : 
            print(0)
    else : 
        heapq.heappush(pq, (abs(k),k))