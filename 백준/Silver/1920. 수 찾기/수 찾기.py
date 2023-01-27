import sys 

def find(k, n, arr):
    left = 0 
    right = n-1 

    while left <= right : 
        middle = (left+right)//2
        if k == arr[middle]:
            return 1
        elif k < arr[middle]:
            right = middle -1
        else : 
            left = middle+1
    return 0


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr.sort()

for ele in arr2 : 
    print(find(ele, n, arr))
