import sys

n = int(sys.stdin.readline())
arr = [
    tuple(map(int, sys.stdin.readline().split())) for _ in range(n)
]

arr.sort(key= lambda x :(-x[0],-x[1]))

count = 0 
check_finish = 0
check_start = 0

for i in range(n):
    if i == 0 : 
        check_finish = arr[i][1]
        check_start = arr[i][0]
        count+=1
    else : 
        if arr[i][1] <= check_start:
            check_finish = arr[i][1]
            check_start = arr[i][0]
            count+=1
print(count)