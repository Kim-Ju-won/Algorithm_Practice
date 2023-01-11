import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
arr_sum = [0]*n
count = 0 

for i in range(n):
    if i == 0 : 
        arr_sum[0] = arr[0]
    else : 
        arr_sum[i] = arr_sum[i-1] + arr[i]
        if arr_sum[i] % m == 0 :
            count += 1

for i in range(n-1):
    for j in range(i+1,n) : 
        arr_sum[j] -= arr[i]
        if arr_sum[j] % m == 0 : 
            count +=1

print(count)
