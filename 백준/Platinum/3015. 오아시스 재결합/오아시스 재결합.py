import sys

n = int(sys.stdin.readline())
arr = [ int(sys.stdin.readline()) for _ in range(n)]
check_list = []
ans = 0 

for i in range(n):
    if i == 0 : 
        check_list.append(arr[i])
    else : 
        if check_list[-1] < arr[i] : 
            while check_list[-1] < arr[i] :
                check = check_list.pop()
                ans+=1
                if check_list and check_list[-1] >= check : 
                    ans+=1
                    if check_list[-1] == check :
                        k = -2 
                        while True:
                            if k*(-1) > len(check_list) : 
                                break
                            if check_list[k] > check :
                                ans+=1
                                break
                            k-=1
                            ans+=1
                if not(check_list) : 
                    break 
        check_list.append(arr[i])
tmp = 0
check = True
count = 1 
for i in range(len(check_list)-1,-1,-1):
    if i == len(check_list)-1 : 
        tmp = check_list[i]
    else : 
        if tmp < check_list[i] : 
            tmp = check_list[i]
            count += 1 
            ans+= count*(count-1)//2
            count = 1
        else : 
            count += 1
            if i == 0 : 
                ans+=count*(count-1)//2


print(ans)