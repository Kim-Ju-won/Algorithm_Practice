import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    ele = int(sys.stdin.readline())
    arr.append(ele)

for i in range(n-1):
    for j in range(i,n):
        if arr[i] > arr[j]:
            arr[i] , arr[j] = arr[j] , arr[i]
for ele in arr : 
    print(ele)