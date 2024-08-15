import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

check_max = -1
check = -1
temp = -1
for i in range(n - 1, 0, -1):
    if arr[i - 1] > arr[i]:
        check_max = i
        check = i - 1
        temp = i
        max_temp = arr[i]
        break

if check_max == -1:
    print(-1)
else:
    for i in range(temp, n):
        if max_temp < arr[i] and arr[check] > arr[i]:
            check_max = i
            max_temp = arr[i]
    arr[check], arr[check_max] = arr[check_max], arr[check]
    for ele in arr[: check + 1] + sorted(arr[check + 1 :], reverse=True):
        print(ele, end=" ")

