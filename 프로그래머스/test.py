
'''
def solution(x, y, z):
    # Write your code here
    if z >= abs(x-y) :
        return max(x,y)+(z-abs(x-y))//2
    else : 
        return -1
'''
'''
def solution(cost, x):
    # Write your code here
    answer = 0
    boundary = min(cost)
    for i in range(len(cost)-1, -1, -1):
        if cost[i] <= x :
            x -= cost[i]
            answer += 2**(i)
            print(i)
    return answer % (10**9+7)
'''
def solution(box):
    # Write your code here
    n = len(box)
    sum_list = [0]*n
    max_list = [0]*n
    
    for i in range(n):
        if i==0 : 
            sum_list = box[0]
            max_list = box[0]
        else : 
            sum_list[i] = sum_list[i-1]+box[i]
            max_list[i] = sum_list[i] // (i+1)
            if sum_list[i] % (i+1) != 0 :
                max_list[i] +=1

    return max(max_list)

print(solution([19,78,27,18,20],25))