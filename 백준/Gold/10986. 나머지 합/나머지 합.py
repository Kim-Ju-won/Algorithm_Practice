import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
sum_arr = n * [0] 
sub_arr = m *[0]

for i in range(n):
    if i == 0 : 
        sum_arr[i] = arr[i]
    else : 
        sum_arr[i] = sum_arr[i-1] + arr[i]

for i in range(n):
    sum_arr[i] %=m
    sub_arr[sum_arr[i]]+=1

ans = 0
for i in range(m):
    if i == 0 :
        ans += sub_arr[i]
    ans +=  sub_arr[i] *(sub_arr[i]-1)//2
print(ans)