import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr_dict = [0]*1000001
for idx in arr  :
    arr_dict[idx]+=1

check_list = []
ans = []
for idx, value in enumerate(arr[-1::-1]):
    idx = n-1-idx
    if idx < n-1 : 
        if arr_dict[value] < arr_dict[arr[idx+1]] : 
            check_list.append(arr[idx+1])
        while check_list : 
            if arr_dict[check_list[-1]] > arr_dict[value] : 
                ans.append(check_list[-1])
                break
            check_list.pop()
        if not(check_list) : 
            ans.append(-1)
    else : 
        ans.append(-1)

for ele in ans[-1::-1]:
    print(ele, end = ' ')