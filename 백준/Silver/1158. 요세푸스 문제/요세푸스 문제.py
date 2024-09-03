import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n + 1)])

answer = "<"
while True:
    q.rotate(-k + 1)
    answer += str(q.popleft())
    if q:
        answer += ", "
    else:
        answer += ">"
        break

print(answer)
