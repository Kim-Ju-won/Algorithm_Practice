def solution(citations):
    
    check_list = 10001*[0]
    answer = 0
    
    for c in citations:
        check_list[c] += 1
    left = 0 
    right = sum(check_list)
    for i in range(1,10001):
        left += check_list[i-1]
        right -= check_list[i-1]
        if right >= i and left <= i : 
            answer = i
    
    return answer
