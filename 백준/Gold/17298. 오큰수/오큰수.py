import sys

n = int(sys.stdin.readline())
arr = list(map(int ,sys.stdin.readline().split()))
check_list = []
ans = []
for i in range(len(arr)-1,-1,-1):
    if i < len(arr)-1 : 
        if arr[i] < arr[i+1] : 
            check_list.append(arr[i+1])
            ans.append(arr[i+1])
        else : 
            no = True
            while check_list : 
                if check_list[-1] > arr[i] : 
                    ans.append(check_list[-1])
                    no = False 
                    break
                check_list.pop()
            if no :
                 ans.append(-1)
    else :
        ans.append(-1)
for ele in ans[-1::-1]:
    print(ele, end = ' ')