def solution(s):
    answer = True
    count_p = 0
    count_y = 0 
    for ele in s : 
        if ele == 'P' or ele =='p': 
            count_p +=1
        elif ele == 'Y' or ele =='y':
            count_y += 1
            
    if count_p != count_y :
        answer = False
    return answer