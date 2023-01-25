def solution(n, k):
    num = 1 
    num_set = set(range(1,n+1))
    for i in range(1,n+1):
        num *= i
    answer = []
    for i in range(n,0,-1):
        num //= i
        tmp = list(num_set)
        tmp.sort()
        if k % num != 0 : 
            answer.append(tmp[k//num])
            num_set.remove(tmp[k//num])
        else : 
            answer.append(tmp[k//num-1])
            num_set.remove(tmp[k//num-1])
        k %= num
    
    return answer