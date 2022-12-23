import sys

n, check  = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if check > arr[i]:
        print(arr[i], end =' ')