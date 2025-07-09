def solution(diffs, times, limit):
    n = len(diffs)
    right= max(diffs)
    left = 1
    answer = 0 
    
    
    while left <= right : 
        level = (right + left) //2
        time_prev = 0 
        check = 0 
        for i in range(n):
            if i != 0 :
                time_prev = times[i-1]
            if level >= diffs[i]:
                check += times[i]
            else : 
                check += (time_prev+times[i])*(diffs[i]-level)+times[i]
        
        if limit >= check :
            answer = level
            right = level - 1
        else : 
            left = level + 1
            
            
    return answer