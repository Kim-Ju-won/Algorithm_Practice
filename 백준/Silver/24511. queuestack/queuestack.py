import sys
from collections import deque

n = int(sys.stdin.readline())
qs_type = list(map(int, sys.stdin.readline().split()))
ele = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
query = list(map(int, sys.stdin.readline().split()))

queue = deque([])

for i, t in enumerate(qs_type):
    if t == 0:
        queue.append(ele[i])

answer = []
for q in query:
    queue.appendleft(q)
    answer.append(queue.pop())

for ele in answer:
    print(ele, end=" ")
