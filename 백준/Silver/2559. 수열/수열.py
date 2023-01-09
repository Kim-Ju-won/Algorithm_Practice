import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

num_arr = [sum(arr[:m])]

for i in range(m,n):
    num_arr.append(num_arr[-1] - arr[i-m] + arr[i])

print(max(num_arr))
