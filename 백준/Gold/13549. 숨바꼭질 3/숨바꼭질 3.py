# 수빈이는 동생과 숨박꼭질 
# 수빈이 점 0<= N<= 100000
# 동생 점 0<=K<=100000

# 수빈이 걷기, 순간이동 
# 걷기: 위치 X, 1초 뒤 X-1, X+1
# 순간이동: 위치 X, 0초 뒤 2*X

import heapq

# 수빈이의 동생의 위치가 주어졌을 때 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 
import sys

sys.setrecursionlimit(10**9)

    
MAX_NUM = int(sys.maxsize)
start, end = tuple(map(int, sys.stdin.readline().split()))
dist = [ MAX_NUM for _ in range(100000+1) ]
pq = []
dist[start] = 0 
count = 0 
heapq.heappush(pq, (0, start))

while pq : 
    min_time, min_index = heapq.heappop(pq)
    
    if min_time == dist[min_index]:
        new_index = min_index
        while new_index != 0 and new_index <= 100000 : 
            new_index = new_index *2 
            if new_index > 100000 : 
                break
            if dist[new_index] > min_time : 
                dist[new_index] = min_time 
                heapq.heappush(pq, (min_time, new_index))
        
                
        if min_index + 1 <= 100000 : 
            if dist[min_index + 1] > min_time + 1 : 
                dist[min_index + 1] = min_time + 1
                heapq.heappush(pq, (min_time+1, min_index+1))
                
        if min_index - 1 >= 0 : 
            if dist[min_index - 1] > min_time + 1 : 
                dist[min_index - 1] = min_time + 1
                heapq.heappush(pq, (min_time+1, min_index-1))
    count +=1

print(dist[end])