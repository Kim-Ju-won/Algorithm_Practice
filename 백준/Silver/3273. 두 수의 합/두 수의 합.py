import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr.sort()
check = 0
i = 0
count = 0
for j in range(n-1,-1,-1):
    check+=arr[j]
    while j > i and check < m : 
        check+=arr[i]
        if check == m : 
            count+=1
        if check > m :
            check-=arr[i]
            break
        check-=arr[i]
        i+=1
    check-=arr[j]

print(count)
