import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for idx, value in enumerate(arr):
    arr[idx] = (value, idx + 1)

arr = deque(arr)
answer = []
while arr:
    rotate, num = arr.popleft()
    answer.append(num)
    if rotate < 0:
        arr.rotate(-rotate)
    else:
        arr.rotate(-rotate + 1)

print(" ".join([str(ele) for ele in answer]))
