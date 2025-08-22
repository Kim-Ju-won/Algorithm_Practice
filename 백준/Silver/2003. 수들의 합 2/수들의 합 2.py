import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))


sum_arr = [0 for _ in range(n)]

count = 0
for i in range(n):
    if i == 0:
        sum_arr[i] = arr[i]
    else:
        sum_arr[i] = sum_arr[i - 1] + arr[i]
    if m == sum_arr[i]:
        count += 1

for i in range(n):
    for j in range(i + 1, n):
        if sum_arr[j] - sum_arr[i] == m:
            count += 1

print(count)
