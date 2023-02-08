import sys

n, s = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

j = 1
check_sum = arr[0]
ans = sys.maxsize

for i in range(n):
    while j < n and check_sum < s :
        check_sum += arr[j]
        j += 1
    if check_sum >= s : 
        ans = min(ans, j-i)
    check_sum -= arr[i]
if ans != sys.maxsize: 
    print(ans)

else : 
    print(0)
