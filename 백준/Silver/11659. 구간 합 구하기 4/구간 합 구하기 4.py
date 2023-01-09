import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = [0]+list(map(int, sys.stdin.readline().split()))

arr_sum = [ 0 for _ in range(n+1)]

for i in range(1,n+1):
    arr_sum[i] = arr_sum[i-1] + arr[i]

for _ in range(m):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(arr_sum[b]-arr_sum[a-1])
