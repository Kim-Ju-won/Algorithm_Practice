import sys

n,m = tuple(map(int,sys.stdin.readline().split()))
nums =  list(map(int, sys.stdin.readline().split()))
nums.sort()
last = set()
def comb(n,m,temp,check_list):
    global last
    if len(temp) == m : 
        if tuple(temp) not in last: 
            for ele in temp : 
                print(ele, end=' ')
            print()
            last.add(tuple(temp))
    else : 
        for i in range(n):
            if i not in check_list :
                temp.append(nums[i])
                check_list.append(i)
                comb(n,m,temp,check_list)
                check_list.pop()
                temp.pop() 

    return 

comb(n,m,[],[])